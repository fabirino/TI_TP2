import functions, lzw, huffman, ppm, rle, mtf, bwt, mtf2

if __name__ == '__main__':
    # functions.BZIP2()

    # lzw.LZW("./dataset\\bible.txt","./resultados\\bible_LZW.bin","./decompress\\decoder_bible_LZW.txt")
    # lzw.LZW("./dataset\\finance.csv","./resultados\\finance_LZW.bin","./decompress\\decoder_finance_LZW.csv")
    # lzw.LZW("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_LZW.bin","./decompress\\decoder_jquery-3.6.0_LZW.js")
    # lzw.LZW("./dataset\\random.txt","./resultados\\random_LZW.bin","./decompress\\decoder_random_LZW.txt")

    # ppm.PPM("./dataset\\bible.txt","./resultados\\bible_PPM.bin","./decompress\\decoder_bible_PPM.txt")
    # ppm.PPM("./dataset\\finance.csv","./resultados\\finance_PPM.bin","./decompress\\decoder_finance_PPM.csv")
    # ppm.PPM("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_PPM.bin","./decompress\\decoder_jquery-3.6.0_PPM.js")
    # ppm.PPM("./dataset\\random.txt","./resultados\\random_PPM.bin","./decompress\\decoder_random_PPM.txt")

    # huffman.huffman("bible.txt")
    # huffman.huffman("finance.csv")
    # huffman.huffman("jquery-3.6.0.js")
    # huffman.huffman("random.txt")

    bwt.BWT("./dataset\\bible.txt", "./resultados\\bible_BWT.bin","./decompress\\decoder_bible_BWT.txt")

    # mtf2.MVF()

    #rle, mtf e nao funcionam ainda
    