# https://titanwolf.org/Network/Articles/Article?AID=2fb527a4-b1a2-4e05-8f56-ad861e0f480e

import pickle
import string

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
    move2front_encode(file, encodefile)
    print(f"Ficheiro \'{file}\' comprimido com MTF")
    move2front_decode(encodefile, decodefile)
    print(f"Ficheiro \'{encodefile}\' descomprimido com MTF")

def allMTF():
    MTF("./dataset\\bible.txt", "./resultados\\bible_MTF.bin","./decompress\\decoder_bible_MTF.txt")
    MTF("./dataset\\finance.csv", "./resultados\\finance_MTF.bin","./decompress\\decoder_finance_MTF.txt")
    MTF("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_MTF.bin","./decompress\\decoder_jquery-3.6.0_MTF.txt")
    MTF("./dataset\\random.txt", "./resultados\\random_MTF.bin","./decompress\\decoder_random_MTF.txt")

# move2front_encode("./dataset\\bible.txt", "./resultados\\bible_MTF.bin")