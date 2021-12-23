# https://stackabuse.com/run-length-encoding/

# rle-encode.py

import time


def rle_encode(infile,outfile):
    data = open(infile, "r").read()
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        encoding += str(count) + prev_char
        with open(outfile, "w") as fp:
            fp.write(encoding)

# rle-decode.py

def rle_decode(infile,outfile):
    data = open(infile, "r").read()
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    with open(outfile, "w") as fp:
        fp.write(decode)


def allRLE():
    print("Comprimindo \'bible.txt\'...")
    tempo =time.time()
    rle_encode("./dataset\\bible.txt", "./resultados\\bible_RLE.bin")
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("Ficheiro \'bible.txt\' comprimido com RLE")
    print("Descomprimindo \'bible.txt\'...")
    tempo2 = time.time()
    rle_decode("./resultados\\bible_RLE.bin","./decompress\\decoder_bible_RLE.txt")
    tempo2 = time.time() - tempo2
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("Ficheiro \'bible_RLE.bin\' descomprimido com RLE")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo = time.time()
    rle_encode("./dataset\\finance.csv", "./resultados\\finance_RLE.bin")
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("Ficheiro \'finance.csv\' comprimido com RLE")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo =time.time()
    rle_encode("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_RLE.bin")
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com RLE")
    print("----------------------------------------------------------------")

    print("Comprimindo\'random.txt\'...")
    tempo =time.time()
    rle_encode("./dataset\\random.txt", "./resultados\\random_RLE.bin")
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("Ficheiro \'random.txt\' comprimido com RLE")
    print("----------------------------------------------------------------")
    print()