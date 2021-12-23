# https://github.com/amycardoso/lzw-text-file-compression/blob/master/lzw.py

import pickle
import time
# função que realiza a compressao da entrada


def compressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}  # armazena o dicionário
    resultado = []  # armazena o resultado comprimido
    temp = ""  # variável que irá armazenar as substrings

    # Adicionando tabela ASCII ao dicionário
    for i in range(0, tamanhoDicionario):
        # Como fica o dicionário {'a': 97, 'b': 98}
        dicionario[str(chr(i))] = i
    # assim podemos percorrer o arquivo, e substituir as substrings por seus respectivos inteiros

    for c in entrada:  # Percorre o arquivo
        # temp2 recebe o caractere atual mais o anterior para verificar se existe no dicionário
        temp2 = temp + str(c)
        if temp2 in dicionario.keys():  # se estiver no dicionário temp = temp2 para ser concatenado posteriormente com o próximo caractere
            temp = temp2
        else:  # caso o conteúdo de temp2 não esteja no dicionário
            # pegamos o inteiro que representa a string anterior no dicionário e adicionamos ao resultado
            resultado.append(dicionario[temp])
            # em seguida adicionamos temp2 ao dicionário
            dicionario[temp2] = tamanhoDicionario
            tamanhoDicionario += 1  # incrementa tamanho do dicionário
            temp = "" + str(c)  # reseta a variável com a substring atual

    if temp != "":  # caso a string temporária não esteja vazia, deve-se adicionar ao resultado
        # pegando o inteiro que a representa no dicionário
        resultado.append(dicionario[temp])

    return resultado


# função que realiza a descompressao da entrada
def descompressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}  # armazena o dicionário
    resultado = []  # armazena o resultado descomprimido

    # inicializando dicionário com tabela ASCII
    for i in range(0, tamanhoDicionario):
        dicionario[i] = str(
            chr(i))  # Como o dicionário fica, ex: {97: 'a', 98: 'b'}, diferente do dicionário de compressão

    anterior = chr(
        entrada[0])  # pega o primeiro caractere e marca como anterior, por exemplo: chr(97) retorna a string 'a'
    entrada = entrada[1:]  # remove o primeiro caractere da entrada
    resultado.append(anterior)  # adiciona o primeiro caractere ao resultado

    for bit in entrada:
        aux = ""
        if bit in dicionario.keys():
            # pega o caractere correspondente ao bit no dicionário
            aux = dicionario[bit]
        else:  # Quando o bit não ta no dicionário, deve se pegar
            # o ultimo caractere impresso + a primeira posição do último caractere impresso
            aux = anterior + anterior[0]
            # pois devemos decodificar bits que não estão presentes no dicionário, então temos que adivinhar o que ele representa, por exemplo:
            # digamos que o bit 37768 não ta no dicionário, então pegamos o último caractere impresso, por exemplo foi 'uh'
            # e pegamos ele 'uh' mais sua primeira posição 'u', resultando em 'uhu', que é a representação do bit 37768
            # o único caso em que isso pode ocorrer é se a substring começar e terminar com o mesmo caractere ("uhuhu").

        resultado.append(aux)  # adiciona ao resultado
        # Resimulando como as substrings foram adicionadas durante a compressão
        # adiciona ao dicionário o caractere anterior mais a primeira posição do caractere atual
        dicionario[tamanhoDicionario] = anterior + aux[0]
        tamanhoDicionario += 1  # incrementa tamanho do dicionário
        anterior = aux  # anterior recebe o caractere atual
    return resultado


def encoderFile(infile, outfile):
    entrada = open(infile, "r").read()
    saida = open(outfile, "wb")
    comprimido = compressao(entrada)
    pickle.dump(comprimido, saida)  # escreve no arquivo binário a compressão
    print(f"Ficheiro \'{infile}\' comprimido com PPM")


def decoderFile(encodefile, decodefile):
    input = pickle.load(open(encodefile, "rb"))
    output = open(decodefile, "w")

    descomprimido = descompressao(input)
    for l in descomprimido:  # grava no arquivo o resultado da descompressão
        output.write(l)
    print(f"Ficheiro \'{encodefile}\' descomprimido com PPM")
    output.close()


def LZW(file, encodefile, decodefile):
    tempo = time.time()
    print(f"Comprimindo \'{file}\'...")
    entrada = open(file, "r").read()
    saida = open(encodefile, "wb")
    comprimido = compressao(entrada)
    pickle.dump(comprimido, saida)  # escreve no arquivo binário a compressão
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    # dump salva o conteúdo serializado do objeto nesse arquivo
    tempo2 = time.time()
    print(f"Descomprimindo \'{encodefile}\'...") 
    input = pickle.load(open(encodefile, "rb"))
    output = open(decodefile, "w")

    descomprimido = descompressao(input)
    for l in descomprimido:  # grava no arquivo o resultado da descompressão
        output.write(l)
    output.close()
    saida.close()
    tempo2 = time.time() - tempo
    print(f"Tempo de descompressao -> {round(tempo2, 4)} segundos")



def allLZW():
    LZW("./dataset\\bible.txt", "./resultados\\bible_LZW.bin",
        "./decompress\\decoder_bible_LZW.txt")
    print("----------------------------------------------------------------")
    LZW("./dataset\\finance.csv", "./resultados\\finance_LZW.bin",
        "./decompress\\decoder_finance_LZW.csv")
    print("----------------------------------------------------------------")
    LZW("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_LZW.bin",
        "./decompress\\decoder_jquery-3.6.0_LZW.js")
    print("----------------------------------------------------------------")
    LZW("./dataset\\random.txt", "./resultados\\random_LZW.bin",
        "./decompress\\decoder_random_LZW.txt")
    print("----------------------------------------------------------------")
    print()

# entrada = open( "./resultados\\random_BWT.txt", "r").read()
# saida = open("./resultados\\random_BWT_LZW.bin", "wb")
# comprimido = compressao(entrada)
# pickle.dump(comprimido, saida)
