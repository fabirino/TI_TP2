# https://titanwolf.org/Network/Articles/Article?AID=2fb527a4-b1a2-4e05-8f56-ad861e0f480e

import pickle
import string
import time

def move2front_encode(infile, outfile):
    strng = open(infile, "r").read()
    symboltable = list(string.printable)
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    with open(outfile, "wb") as fp:
        pickle.dump(sequence, fp)

def move2front_decode(infile, outfile):
    with open(infile, "rb") as fp:
        fi = pickle.load(fp)
    symboltable = list(string.printable)
    chars, pad = [], symboltable[::]
    for indx in fi:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    with open(outfile, "w") as fp:
        fp.write(''.join(chars))
    return ''.join(chars)

def MTF(file,encodefile,decodefile):
    print(f"Comprimindo \'{file}\'...")
    tempo = time.time()
    move2front_encode(file, encodefile)
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print(f"Ficheiro \'{file}\' comprimido com MTF")

    print(f"Descomprimindo \'{encodefile}\'...")
    tempo2 = time.time()
    move2front_decode(encodefile, decodefile)
    tempo2 = time.time() - tempo2
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print(f"Ficheiro \'{encodefile}\' descomprimido com MTF")

def allMTF():
    MTF("./dataset\\bible.txt", "./resultados\\bible_MTF.bin","./decompress\\decoder_bible_MTF.txt")
    print("----------------------------------------------------------------")
    MTF("./dataset\\finance.csv", "./resultados\\finance_MTF.bin","./decompress\\decoder_finance_MTF.txt")
    print("----------------------------------------------------------------")
    MTF("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_MTF.bin","./decompress\\decoder_jquery-3.6.0_MTF.txt")
    print("----------------------------------------------------------------")
    MTF("./dataset\\random.txt", "./resultados\\random_MTF.bin","./decompress\\decoder_random_MTF.txt")
    print("----------------------------------------------------------------")
    print()
# move2front_encode("./dataset\\bible.txt", "./resultados\\bible_MTF.bin")