from os import system
import functions,huffman,lzw,ppm,mtf,rle,bwt

def BWT_RLE():
    bwt.encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    rle.rle_encode("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_RLE.bin")
    print("Ficheiro \'bible_BWT.txt\' comprimido com RLE")

    bwt.encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    rle.rle_encode("./resultados\\finance_BWT.txt","./resultados\\finance_BWT_RLE.bin")
    print("Ficheiro \'finance_BWT.txt\' comprimido com RLE")

    bwt.encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    rle.rle_encode("./resultados\\jquery-3.6.0_BWT.txt","./resultados\\jquery-3.6.0_BWT_RLE.bin")
    print("Ficheiro \'jquery-3.6.0_BWT.txt\' comprimido com RLE")

    bwt.encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    rle.rle_encode("./resultados\\random_BWT.txt","./resultados\\random_BWT_RLE.bin")
    print("Ficheiro \'random_BWT.txt\' comprimido com RLE")


def LZW_BZIP():
    lzw.encoderFile("./dataset\\bible.txt","./resultados\\bible_LZW.bin")
    functions.encoderFile("./resultados\\bible_LZW.bin","./resultados\\bible_LZW_BZ2.bin")
    print("Ficheiro \'bible_LZW.bin\' comprimido com BZIP")

    lzw.encoderFile("./dataset\\finance.csv","./resultados\\finance_LZW.bin")
    functions.encoderFile("./resultados\\finance_LZW.bin","./resultados\\finance_LZW_BZ2.bin")
    print("Ficheiro \'finance_LZW.bin\' comprimido com BZIP")

    lzw.encoderFile("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_LZW.bin")
    functions.encoderFile("./resultados\\jquery-3.6.0_LZW.bin","./resultados\\jquery-3.6.0_LZW_BZ2.bin")
    print("Ficheiro \'bible_LZW.bin\' comprimido com BZIP")

    lzw.encoderFile("./dataset\\random.txt","./resultados\\random_LZW.bin")
    functions.encoderFile("./resultados\\random_LZW.bin","./resultados\\random_LZW_BZ2.bin")
    print("Ficheiro \'random_LZW.bin\' comprimido com BZIP")


def BWT_PPM():
    bwt.encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_PPM.bin")
    print(f"Ficheiro \'bible_BWT.txt\' comprimido com PPM")

    bwt.encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\finance_BWT.txt","./resultados\\finance_BWT_PPM.bin")
    print("Ficheiro \'finance_BWT.txt\' comprimido com PPM")

    bwt.encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\jquery-3.6.0_BWT.txt","./resultados\\jquery-3.6.0_BWT_PPM.bin")
    print("Ficheiro \'jquery-3.6.0_BWT.txt\' comprimido com PPM")

    bwt.encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\random_BWT.txt","./resultados\\random_BWT_PPM.bin")
    print("Ficheiro \'random_BWT.txt\' comprimido com PPM")

def Huff_Bzip():
    huffman.Huffman()
    functions.encoderFile("./resultados\\bible_Huff.bin","./resultados\\bible_Huff_Bz2.bin")
    print("Ficheiro \'bible_Huff.bin\' comprimido com BZIP")
    functions.encoderFile("./resultados\\finance_Huff.bin","./resultados\\finance_Huff_Bz2.bin")
    print("Ficheiro \'finance_Huff.bin\' comprimido com BZIP")
    functions.encoderFile("./resultados\\jquery-3.6.0_Huff.bin","./resultados\\jquery-3.6.0_Huff_Bz2.bin")
    print("Ficheiro \'jquery-3.6.0_Huff.bin\' comprimido com BZIP")
    functions.encoderFile("./resultados\\random_Huff.bin","./resultados\\random_Huff_Bz2.bin")
    print("Ficheiro \'random_Huff.bin\' comprimido com BZIP")


def BWT_LZW():
    bwt.encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    lzw.encoderFile("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_LZW.bin")
    print(f"Ficheiro \'bible_BWT.txt\' comprimido com LZW")

    bwt.encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    lzw.encoderFile("./resultados\\finance_BWT.txt","./resultados\\finance_BWT_LZW.bin")
    print("Ficheiro \'finance_BWT.txt\' comprimido com PPM")

    bwt.encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    lzw.encoderFile("./resultados\\jquery-3.6.0_BWT.txt","./resultados\\jquery-3.6.0_BWT_LZW.bin")    
    print("Ficheiro \'jquery-3.6.0_BWT.txt\' comprimido com PPM")

    bwt.encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    lzw.encoderFile("./resultados\\random_BWT.txt","./resultados\\random_BWT_LZW.bin")    
    print("Ficheiro \'random_BWT.txt\' comprimido com PPM")



while(True):
    print("Menu:\n0 - Sair\n1 - Bzip2\n2 - Huffman\n3 - LZW\n4 - PPM\n5 - MTF\n6 - RLE\n7 - BWT\n8 - BWT->RLE\n9 -  LZW -> BZIP\n10 - BWT -> PPM\n11 - Huffman -> Bzip\n12 - BWT -> LZW")
    escolha = int(input("Escolha um numero: "))
    if(escolha == 1):
        functions.BZIP2()
    elif(escolha == 2):
        huffman.Huffman()
    elif(escolha == 3):
        lzw.allLZW()
    elif(escolha == 4):
        ppm.allPPM()
    elif(escolha == 5):
        mtf.allMTF()
    elif(escolha == 6):
        rle.allRLE()
    elif(escolha == 7):
        bwt.allBWT()
    elif(escolha == 8):
        BWT_RLE()
    elif(escolha == 9):
        LZW_BZIP()
    elif(escolha == 10):
        BWT_PPM()
    elif(escolha == 11):
        Huff_Bzip()
    elif(escolha == 12):
        BWT_LZW()
    elif(escolha == 0):
        break
    else:
        continue
