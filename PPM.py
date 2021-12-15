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

encoderPPM('./dataset\\bible.txt','./resultados\\bibleppm.bin')

def decoderPPM(data,dataout):
    targetfile = pathlib.Path(data)
    with open(targetfile, 'rb') as target:
        with ppmd.PpmdDecompressor(target, targetfile.stat().st_size) as decompressor:
            with open(dataout, 'wb') as ofile:
                decompressor.decompress(ofile)
            timestamp = ppmd.datetime_to_timestamp(decompressor.ftime)

decoderPPM('./resultados\\bibleppm.bin','./resultados\\decoderbibleppm.bin')