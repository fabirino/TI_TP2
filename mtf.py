# https://www.ti-enxame.com/pt/python/como-salvar-uma-lista-em-um-arquivo-e-le-lo-como-um-tipo-de-lista/1049890256/

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
    move2front_decode(encodefile, decodefile)

move2front_encode("./dataset\\bible.txt", "./resultados\\bible_MTF.bin")