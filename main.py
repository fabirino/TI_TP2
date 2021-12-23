import functions,huffman,lzw,ppm,mtf,rle,bwt
import time

def BWT_RLE():
    print("Comprimindo \'bible.txt\'...")
    tempo = time.time()
    bwt.encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    rle.rle_encode("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_RLE.bin")
    tempo = time.time() - tempo
    print("Ficheiro \'bible_BWT.txt\' comprimido com RLE")
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo2 = time.time()
    bwt.encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    rle.rle_encode("./resultados\\finance_BWT.txt","./resultados\\finance_BWT_RLE.bin")
    tempo2 = time.time() - tempo2
    print("Ficheiro \'finance_BWT.txt\' comprimido com RLE")
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo3 = time.time()
    bwt.encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    rle.rle_encode("./resultados\\jquery-3.6.0_BWT.txt","./resultados\\jquery-3.6.0_BWT_RLE.bin")
    tempo3 = time.time() - tempo3
    print("Ficheiro \'jquery-3.6.0_BWT.txt\' comprimido com RLE")
    print(f"Tempo de compressao -> {round(tempo3, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'random.txt\'...")
    tempo4 = time.time()
    bwt.encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    rle.rle_encode("./resultados\\random_BWT.txt","./resultados\\random_BWT_RLE.bin")
    tempo4 = time.time() - tempo4
    print("Ficheiro \'random_BWT.txt\' comprimido com RLE")
    print(f"Tempo de compressao -> {round(tempo4, 4)} segundos")
    print("----------------------------------------------------------------")

def LZW_BZIP():
    print("Comprimindo \'bible.txt\'...")
    tempo = time.time()
    lzw.encoderFile("./dataset\\bible.txt","./resultados\\bible_LZW.bin")
    functions.encoderFile("./resultados\\bible_LZW.bin","./resultados\\bible_LZW_BZ2.bin")
    tempo = time.time() - tempo
    print("Ficheiro \'bible_LZW.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo2 = time.time()
    lzw.encoderFile("./dataset\\finance.csv","./resultados\\finance_LZW.bin")
    functions.encoderFile("./resultados\\finance_LZW.bin","./resultados\\finance_LZW_BZ2.bin")
    tempo2 = time.time() - tempo2
    print("Ficheiro \'finance_LZW.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo3 = time.time()
    lzw.encoderFile("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_LZW.bin")
    functions.encoderFile("./resultados\\jquery-3.6.0_LZW.bin","./resultados\\jquery-3.6.0_LZW_BZ2.bin")
    tempo3 = time.time() - tempo3
    print("Ficheiro \'bible_LZW.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo3, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'random.txt\'...")
    tempo4 = time.time()
    lzw.encoderFile("./dataset\\random.txt","./resultados\\random_LZW.bin")
    functions.encoderFile("./resultados\\random_LZW.bin","./resultados\\random_LZW_BZ2.bin")
    tempo4 = time.time() - tempo4
    print("Ficheiro \'random_LZW.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo4, 4)} segundos")
    print("----------------------------------------------------------------")


def BWT_PPM():
    print("Comprimindo \'bible.txt\'...")
    tempo = time.time()
    bwt.encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_PPM.bin")
    tempo = time.time() - tempo
    print(f"Ficheiro \'bible_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo2 = time.time()
    bwt.encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\finance_BWT.txt","./resultados\\finance_BWT_PPM.bin")
    tempo2 = time.time() - tempo2
    print("Ficheiro \'finance_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo3 = time.time()
    bwt.encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\jquery-3.6.0_BWT.txt","./resultados\\jquery-3.6.0_BWT_PPM.bin")
    tempo3 = time.time() - tempo3
    print("Ficheiro \'jquery-3.6.0_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo3, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'random.txt\'...")
    tempo4 = time.time()
    bwt.encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    ppm.encoderPPM("./resultados\\random_BWT.txt","./resultados\\random_BWT_PPM.bin")
    tempo4 = time.time() - tempo4
    print("Ficheiro \'random_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo4, 4)} segundos")
    print("----------------------------------------------------------------")

def Huff_Bzip():
    print("Comprimindo \'bible.txt\'...")
    tempo = time.time()
    huffman.HuffmanEncode("./dataset\\bible.txt", "./resultados\\bible_Huff.bin", "./dicionarios\\bible_Huff.bin")
    functions.encoderFile("./resultados\\bible_Huff.bin","./resultados\\bible_Huff_Bz2.bin")
    tempo = time.time() - tempo
    print("Ficheiro \'bible_Huff.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo2 = time.time()
    huffman.HuffmanEncode("./dataset\\finance.csv", "./resultados\\finance_Huff.bin", "./dicionarios\\finance_Huff.bin")
    functions.encoderFile("./resultados\\finance_Huff.bin","./resultados\\finance_Huff_Bz2.bin")
    tempo2 = time.time() - tempo2
    print("Ficheiro \'finance_Huff.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo3 = time.time()
    huffman.HuffmanEncode("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_Huff.bin", "./dicionarios\\jquery-3.6.0_Huff.bin")
    functions.encoderFile("./resultados\\jquery-3.6.0_Huff.bin","./resultados\\jquery-3.6.0_Huff_Bz2.bin")
    tempo3 = time.time() - tempo3
    print("Ficheiro \'jquery-3.6.0_Huff.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo3, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'random.txt\'...")
    tempo4 = time.time()
    huffman.HuffmanEncode("./dataset\\random.txt", "./resultados\\random_Huff.bin", "./dicionarios\\random_Huff.bin")
    functions.encoderFile("./resultados\\random_Huff.bin","./resultados\\random_Huff_Bz2.bin")
    tempo4 = time.time() - tempo4
    print("Ficheiro \'random_Huff.bin\' comprimido com BZIP")
    print(f"Tempo de compressao -> {round(tempo4, 4)} segundos")
    print("----------------------------------------------------------------")


def BWT_LZW():
    print("Comprimindo \'bible.txt\'...")
    tempo = time.time()
    bwt.encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    lzw.encoderFile("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_LZW.bin")
    tempo = time.time() - tempo
    print(f"Ficheiro \'bible_BWT.txt\' comprimido com LZW")
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo2 = time.time()
    bwt.encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    lzw.encoderFile("./resultados\\finance_BWT.txt","./resultados\\finance_BWT_LZW.bin")
    tempo2 = time.time() - tempo2
    print("Ficheiro \'finance_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo3 = time.time()
    bwt.encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    lzw.encoderFile("./resultados\\jquery-3.6.0_BWT.txt","./resultados\\jquery-3.6.0_BWT_LZW.bin") 
    tempo3 = time.time() - tempo3  
    print("Ficheiro \'jquery-3.6.0_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo3, 4)} segundos")
    print("----------------------------------------------------------------")

    print("Comprimindo \'random.txt\'...")
    tempo4 = time.time()
    bwt.encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    lzw.encoderFile("./resultados\\random_BWT.txt","./resultados\\random_BWT_LZW.bin") 
    tempo4 = time.time() - tempo4   
    print("Ficheiro \'random_BWT.txt\' comprimido com PPM")
    print(f"Tempo de compressao -> {round(tempo4, 4)} segundos")
    print("----------------------------------------------------------------")



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
