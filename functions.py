import numpy as np
from operator import itemgetter
from decimal import Decimal
import bz2
import time

'''ENTROPIA'''

def calcula_ocorrencias(Fonte):
    dic = {}
    ocorrencias = []
    for i in Fonte:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic.setdefault(i, 1)
    for v in dic.values():
        ocorrencias.append(v)
    return ocorrencias


def calcula_entropia(tabOcorrencias):
    entropia = 0
    ocorrencias = tabOcorrencias
    ocorrencias = np.copy(ocorrencias)
    ocorrencias = ocorrencias[ocorrencias != 0]
    soma = np.sum(ocorrencias)
    entropia = np.sum((ocorrencias/soma) * np.log2(ocorrencias/soma))
    return abs(entropia)


'''TRANSFORAMDAS E METODOS DE COMPRESSAO'''
# LZ-78 (copiado de um repostitorio do github) =============================

def encodeLZ(FileIn, FileOut):
    input_file = open(FileIn, 'r')
    encoded_file = open(FileOut, 'w')
    text_from_file = input_file.read()
    dict_of_codes = {text_from_file[0]: '1'}
    encoded_file.write('0' + text_from_file[0])
    text_from_file = text_from_file[1:]
    combination = ''
    code = 2
    for char in text_from_file:
        combination += char
        if combination not in dict_of_codes:
            dict_of_codes[combination] = str(code)
            if len(combination) == 1:
                encoded_file.write('0' + combination)
            else:
                encoded_file.write(
                    dict_of_codes[combination[0:-1]] + combination[-1])
            code += 1
            combination = ''
    input_file.close()
    encoded_file.close()
    return True


def decodeLZ(FileIn, FileOut):
    coded_file = open(FileIn, 'r')
    decoded_file = open(FileOut, 'w')
    text_from_file = coded_file.read()
    dict_of_codes = {'0': '', '1': text_from_file[1]}
    decoded_file.write(dict_of_codes['1'])
    text_from_file = text_from_file[2:]
    combination = ''
    code = 2
    for char in text_from_file:
        if char in '1234567890':
            combination += char
        else:
            dict_of_codes[str(code)] = dict_of_codes[combination] + char
            decoded_file.write(dict_of_codes[combination] + char)
            combination = ''
            code += 1
    coded_file.close()
    decoded_file.close()



# Codigos Aritmeticos ======================================================

class ArithmeticEncoding:
    """
    ArithmeticEncoding is a class for building the arithmetic encoding.
    """

    def __init__(self, frequency_table, save_stages=False):
        """
        frequency_table: Frequency table as a dictionary where key is the symbol and value is the frequency.
        save_stages: If True, then the intervals of each stage are saved in a list. Note that setting save_stages=True may cause memory overflow if the message is large
        """

        self.save_stages = save_stages
        if(save_stages == True):
            print(
                "WARNING: Setting save_stages=True may cause memory overflow if the message is large.")

        self.probability_table = self.get_probability_table(frequency_table)

    def get_probability_table(self, frequency_table):
        """
        Calculates the probability table out of the frequency table.

        frequency_table: A table of the term frequencies.

        Returns the probability table.
        """
        total_frequency = sum(list(frequency_table.values()))

        probability_table = {}
        for key, value in frequency_table.items():
            probability_table[key] = value/total_frequency

        return probability_table

    def get_encoded_value(self, last_stage_probs):
        """
        After encoding the entire message, this method returns the single value that represents the entire message.

        last_stage_probs: A list of the probabilities in the last stage.

        Returns the minimum and maximum probabilites in the last stage in addition to the value encoding the message.
        """
        last_stage_probs = list(last_stage_probs.values())
        last_stage_values = []
        for sublist in last_stage_probs:
            for element in sublist:
                last_stage_values.append(element)

        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)
        encoded_value = (last_stage_min + last_stage_max)/2

        return last_stage_min, last_stage_max, encoded_value

    def process_stage(self, probability_table, stage_min, stage_max):
        """
        Processing a stage in the encoding/decoding process.

        probability_table: The probability table.
        stage_min: The minumim probability of the current stage.
        stage_max: The maximum probability of the current stage.

        Returns the probabilities in the stage.
        """

        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(probability_table.items())):
            term = list(probability_table.keys())[term_idx]
            term_prob = Decimal(probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        return stage_probs

    def encode(self, msg, probability_table):
        """
        Encodes a message using arithmetic encoding.

        msg: The message to be encoded.
        probability_table: The probability table.

        Returns the encoder, the floating-point value representing the encoded message, and the maximum and minimum values of the interval in which the floating-point value falls.
        """

        msg = list(msg)

        encoder = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for msg_term_idx in range(len(msg)):
            stage_probs = self.process_stage(
                probability_table, stage_min, stage_max)

            msg_term = msg[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            if self.save_stages:
                encoder.append(stage_probs)

        last_stage_probs = self.process_stage(
            probability_table, stage_min, stage_max)

        if self.save_stages:
            encoder.append(last_stage_probs)

        interval_min_value, interval_max_value, encoded_msg = self.get_encoded_value(
            last_stage_probs)

        return encoded_msg, encoder, interval_min_value, interval_max_value

    def process_stage_binary(self, float_interval_min, float_interval_max, stage_min_bin, stage_max_bin):
        """
        Processing a stage in the encoding/decoding process.

        float_interval_min: The minimum floating-point value in the interval in which the floating-point value that encodes the message is located.
        float_interval_max: The maximum floating-point value in the interval in which the floating-point value that encodes the message is located.
        stage_min_bin: The minimum binary number in the current stage.
        stage_max_bin: The maximum binary number in the current stage.

        Returns the probabilities of the terms in this stage. There are only 2 terms.
        """

        stage_mid_bin = stage_min_bin + "1"
        stage_min_bin = stage_min_bin + "0"

        stage_probs = {}
        stage_probs[0] = [stage_min_bin, stage_mid_bin]
        stage_probs[1] = [stage_mid_bin, stage_max_bin]

        return stage_probs

    def encode_binary(self, float_interval_min, float_interval_max):
        """
        Calculates the binary code that represents the floating-point value that encodes the message.

        float_interval_min: The minimum floating-point value in the interval in which the floating-point value that encodes the message is located.
        float_interval_max: The maximum floating-point value in the interval in which the floating-point value that encodes the message is located.

        Returns the binary code representing the encoded message.
        """

        binary_encoder = []
        binary_code = None

        stage_min_bin = "0.0"
        stage_max_bin = "1.0"

        stage_probs = {}
        stage_probs[0] = [stage_min_bin, "0.1"]
        stage_probs[1] = ["0.1", stage_max_bin]

        while True:
            if float_interval_max < bin2float(stage_probs[0][1]):
                stage_min_bin = stage_probs[0][0]
                stage_max_bin = stage_probs[0][1]
            else:
                stage_min_bin = stage_probs[1][0]
                stage_max_bin = stage_probs[1][1]

            if self.save_stages:
                binary_encoder.append(stage_probs)

            stage_probs = self.process_stage_binary(float_interval_min,
                                                    float_interval_max,
                                                    stage_min_bin,
                                                    stage_max_bin)

            # print(stage_probs[0][0], bin2float(stage_probs[0][0]))
            # print(stage_probs[0][1], bin2float(stage_probs[0][1]))
            if (bin2float(stage_probs[0][0]) >= float_interval_min) and (bin2float(stage_probs[0][1]) < float_interval_max):
                # The binary code is found.
                # print(stage_probs[0][0], bin2float(stage_probs[0][0]))
                # print(stage_probs[0][1], bin2float(stage_probs[0][1]))
                # print("The binary code is : ", stage_probs[0][0])
                binary_code = stage_probs[0][0]
                break
            elif (bin2float(stage_probs[1][0]) >= float_interval_min) and (bin2float(stage_probs[1][1]) < float_interval_max):
                # The binary code is found.
                # print(stage_probs[1][0], bin2float(stage_probs[1][0]))
                # print(stage_probs[1][1], bin2float(stage_probs[1][1]))
                # print("The binary code is : ", stage_probs[1][0])
                binary_code = stage_probs[1][0]
                break

        if self.save_stages:
            binary_encoder.append(stage_probs)

        return binary_code, binary_encoder

    def decode(self, encoded_msg, msg_length, probability_table):
        """
        Decodes a message from a floating-point number.

        encoded_msg: The floating-point value that encodes the message.
        msg_length: Length of the message.
        probability_table: The probability table.

        Returns the decoded message.
        """

        decoder = []

        decoded_msg = []

        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)

        for idx in range(msg_length):
            stage_probs = self.process_stage(
                probability_table, stage_min, stage_max)

            for msg_term, value in stage_probs.items():
                if encoded_msg >= value[0] and encoded_msg <= value[1]:
                    break

            decoded_msg.append(msg_term)

            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]

            if self.save_stages:
                decoder.append(stage_probs)

        if self.save_stages:
            last_stage_probs = self.process_stage(
                probability_table, stage_min, stage_max)
            decoder.append(last_stage_probs)

        return decoded_msg, decoder


def float2bin(float_num, num_bits=None):
    """
    Converts a floating-point number into binary.

    float_num: The floating-point number. 
    num_bits: The number of bits expected in the result. If None, then the number of bits depends on the number.

    Returns the binary representation of the number.
    """

    float_num = str(float_num)
    if float_num.find(".") == -1:
        # No decimals in the floating-point number.
        integers = float_num
        decimals = ""
    else:
        integers, decimals = float_num.split(".")
    decimals = "0." + decimals
    decimals = Decimal(decimals)
    integers = int(integers)

    result = ""
    num_used_bits = 0
    while True:
        mul = decimals * 2
        int_part = int(mul)
        result = result + str(int_part)
        num_used_bits = num_used_bits + 1

        decimals = mul - int(mul)
        if type(num_bits) is type(None):
            if decimals == 0:
                break
        elif num_used_bits >= num_bits:
            break
    if type(num_bits) is type(None):
        pass
    elif len(result) < num_bits:
        num_remaining_bits = num_bits - len(result)
        result = result + "0"*num_remaining_bits

    integers_bin = bin(integers)[2:]
    result = str(integers_bin) + "." + str(result)
    return result


def bin2float(bin_num):
    """
    Converts a binary number to a floating-point number.

    bin_num: The binary number as a string.

    Returns the floating-point representation.
    """

    if bin_num.find(".") == -1:
        # No decimals in the binary number.
        integers = bin_num
        decimals = ""
    else:
        integers, decimals = bin_num.split(".")
    result = Decimal(0.0)

    # Working with integers.
    for idx, bit in enumerate(integers):
        if bit == "0":
            continue
        mul = 2**idx
        result = result + Decimal(mul)

    # Working with decimals.
    for idx, bit in enumerate(decimals):
        if bit == "0":
            continue
        mul = Decimal(1.0)/Decimal((2**(idx+1)))
        result = result + mul
    return result


'''lEITURA E ESCRITA DE NOVOS FICHEIROS'''

def decoderBZIP2(filename,fileout):
    tempo = time.time()
    with open(fileout, 'w') as f:
        bintoStr = str(bz2.open(filename,'r').read())[2:-1]
        spl = bintoStr.split("\\n")
        f.write("\n".join(spl).replace("\t"," "))
    tempo =  time.time()-tempo 
    print(f"Tempo de descompressao -> {round(tempo, 4)} segundos")

def BZIP2():
    tempo11 = time.time()
    print("Comprimindo \'bible.txt\'...")
    with open("./dataset\\bible.txt", 'r') as bible, open("./resultados\\bible_BZ2.bin", "wb") as bible_bz2:
        texto1 = bible.read()
        compress = bz2.compress(texto1.encode('ascii'), compresslevel=9)
        bible_bz2.write(bytes(compress))
    tempo11 =  time.time()-tempo11 
    print(f"Tempo de compressao -> {round(tempo11, 4)} segundos")
    print("Ficheiro \'bible.txt\' comprimido com BZIP")
    print("Descomprimindo \'bible_BZ2.bin\'...")
    tempo12 = time.time()
    decoderBZIP2("./resultados\\bible_bz2.bin","./decompress\\decoder_bible_bz2.txt")
    tempo12 =  time.time()-tempo12
    print(f"Tempo de descompressao -> {round(tempo12, 4)} segundos")
    print("Ficheiro \'bible_BZ2.bin\' descomprimido com BZIP")
    print("----------------------------------------------------------------")

    tempo21 = time.time()
    print("Comprimindo \'finance.csv\'...")
    with open("./dataset\\finance.csv" , 'r') as finance, open("./resultados\\finance_BZ2.bin", "wb") as finance_bz2:
        texto2 = finance.read()
        compress_finance = bz2.compress(texto2.encode('ascii'), compresslevel=9)
        finance_bz2.write(bytes(compress_finance))
    tempo21 =  time.time()-tempo21 
    print(f"Tempo de compressao -> {round(tempo21, 4)} segundos")
    print("Ficheiro \'finance.csv\' comprimido com BZIP")
    print("Descomprimindo \'finance_BZ2.bin\'...")
    tempo22 = time.time()
    decoderBZIP2("./resultados\\finance_bz2.bin","./decompress\\decoder_finance_bz2.csv")
    tempo22 =  time.time()-tempo22 
    print(f"Tempo de descompressao -> {round(tempo22, 4)} segundos")
    print("Ficheiro \'finance_BZ2.bin\' descomprimido com BZIP")
    print("----------------------------------------------------------------")

    tempo31 = time.time()
    print("Comprimindo \'random.txt\'...")
    with open("./dataset\\random.txt", 'r') as random, open("./resultados\\random_bz2.bin", 'wb') as random_bz2:
        texto3 = random.read()
        compress_random = bz2.compress(texto3.encode('ascii'), compresslevel=9)
        random_bz2.write(bytes(compress_random))
    tempo31= time.time() - tempo31
    print(f"Tempo de compressao -> {round(tempo31, 4)} segundos")
    print("Ficheiro \'random.txt\' comprimido com BZIP")
    print("Descomprimindo \'random_bz2.bin\'...")
    tempo32 = time.time()
    decoderBZIP2("./resultados\\random_bz2.bin","./decompress\\decoder_random_bz2.txt")
    tempo32 = time.time() - tempo32
    print(f"Tempo de descompressao -> {round(tempo32, 4)} segundos")
    print("Ficheiro \'random_bz2.bin\' descomprimido com BZIP")
    print("----------------------------------------------------------------")

    tempo41 = time.time()
    print("Comprimindo \'jquery-3.6.0.js\'...")
    with open("./dataset\\jquery-3.6.0.js", 'r') as jquery, open("./resultados\\jquery_bz2.bin", 'wb') as jquery_bz2:
        texto4 = jquery.read()
        compress_jquery =bz2.compress(texto4.encode('ascii'), compresslevel=9)
        jquery_bz2.write(bytes(compress_jquery))
    tempo41 = time.time() - tempo41
    print(f"Tempo de compressao -> {round(tempo41, 4)} segundos")
    print("Ficheiro \'jquery-3.6.0.js\'  comprimido com BZIP")
    print("Descomprimindo \'jquery_bz2.bin\'...")
    tempo42 = time.time()
    decoderBZIP2("./resultados\\jquery_bz2.bin","./decompress\\decoder_jquery_bz2.js")
    tempo42 = time.time() - tempo42
    print(f"Tempo de descompressao -> {round(tempo42, 4)} segundos")
    print("Ficheiro \'jquery_bz2.bin\' descomprimido com BZIP")
    print("----------------------------------------------------------------")
    print()
    
def encoderFile(infile,outfile):
    with open(infile,"rb") as lz,open(outfile, 'wb') as bzip:
        ti = lz.read()
        compress = bz2.compress(ti,compresslevel=9)
        bzip.write(bytes(compress))
    