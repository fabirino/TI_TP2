# https://ppmd-cffi.readthedocs.io/_/downloads/en/stable/pdf/

import pathlib
from datetime import datetime
import ppmd

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
    encoderPPM(file,encodefile)
    print(f"Ficheiro \'{file}\' comprimido com PPM")
    decoderPPM(encodefile,decodefile)
    print(f"Ficheiro \'{encodefile}\' descomprimido com PPM")


def allPPM():
    PPM("./dataset\\bible.txt","./resultados\\bible_PPM.bin","./decompress\\decoder_bible_PPM.txt")
    PPM("./dataset\\finance.csv","./resultados\\finance_PPM.bin","./decompress\\decoder_finance_PPM.csv")
    PPM("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_PPM.bin","./decompress\\decoder_jquery-3.6.0_PPM.js")
    PPM("./dataset\\random.txt","./resultados\\random_PPM.bin","./decompress\\decoder_random_PPM.txt")


# encoderPPM("./resultados\\bible_BWT.txt","./resultados\\bible_BWT_PPM.bin")