import functions,lzw,huffman,ppm

if __name__ == '__main__':
    functions.BZIP2()

    lzw.LZW("./dataset\\bible.txt","./resultados\\biblelzw.bin","./decompress\\decoder_biblelzw.txt")
    lzw.LZW("./dataset\\finance.csv","./resultados\\financelzw.bin","./decompress\\decoder_financelzw.csv")
    lzw.LZW("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0lzw.bin","./decompress\\decoder_jquery-3.6.0lzw.js")
    lzw.LZW("./dataset\\random.txt","./resultados\\randomlzw.bin","./decompress\\decoder_randomlzw.txt")

    ppm.PPM("./dataset\\bible.txt","./resultados\\biblePPM.bin","./decompress\\decoder_biblePPM.txt")
    ppm.PPM("./dataset\\finance.csv","./resultados\\financePPM.bin","./decompress\\decoder_financePPM.csv")
    ppm.PPM("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0PPM.bin","./decompress\\decoder_jquery-3.6.0PPM.js")
    ppm.PPM("./dataset\\random.txt","./resultados\\randomPPM.bin","./decompress\\decoder_randomPPM.txt")
    huffman.huffman("bible.txt")
    huffman.huffman("finance.csv")
    huffman.huffman("jquery-3.6.0.js")
    huffman.huffman("random.txt")
