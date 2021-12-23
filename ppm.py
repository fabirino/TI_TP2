# https://ppmd-cffi.readthedocs.io/_/downloads/en/stable/pdf/

import pathlib
from datetime import datetime
import ppmd
import time

def encoderPPM(data,dataout):
    targetfile = pathlib.Path(data)
    fname = data
    ftime = datetime.utcfromtimestamp(targetfile.stat().st_mtime)
    order = 6
    mem_in_mb = 8
    with open(dataout, 'wb') as target:
        with open(targetfile, 'rb') as src:
            with ppmd.PpmdCompressor(target, fname, ftime, order, mem_in_mb, version=8) as compressor:
                compressor.compress(src)

def decoderPPM(data,dataout):
    targetfile = pathlib.Path(data)
    with open(targetfile, 'rb') as target:
        with ppmd.PpmdDecompressor(target, targetfile.stat().st_size) as decompressor:
            with open(dataout, 'wb') as ofile:
                decompressor.decompress(ofile)
            timestamp = ppmd.datetime_to_timestamp(decompressor.ftime)

def PPM(file,encodefile,decodefile):
    print(f"Comprimindo \'{file}\'...")
    tempo = time.time()
    encoderPPM(file,encodefile)
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print(f"Ficheiro \'{file}\' comprimido com PPM")
    
    print(f"Descomprimindo \'{encodefile}\'...")
    tempo2 = time.time()
    decoderPPM(encodefile,decodefile)
    tempo2 = time.time() - tempo2
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print(f"Ficheiro \'{encodefile}\' descomprimido com PPM")


def allPPM():
    PPM("./dataset\\bible.txt","./resultados\\bible_PPM.bin","./decompress\\decoder_bible_PPM.txt")
    print("----------------------------------------------------------------")
    PPM("./dataset\\finance.csv","./resultados\\finance_PPM.bin","./decompress\\decoder_finance_PPM.csv")
    print("----------------------------------------------------------------")
    PPM("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_PPM.bin","./decompress\\decoder_jquery-3.6.0_PPM.js")
    print("----------------------------------------------------------------")
    PPM("./dataset\\random.txt","./resultados\\random_PPM.bin","./decompress\\decoder_random_PPM.txt")
    print("----------------------------------------------------------------")
    print()

# encoderPPM("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_PPM.bin")