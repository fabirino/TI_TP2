# https://stackabuse.com/run-length-encoding/

# rle-encode.py

def rle_encode(infile,outfile):
    data = open(infile, "r").read()
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        encoding += str(count) + prev_char
        with open(outfile, "w") as fp:
            fp.write(encoding)

# rle-decode.py

def rle_decode(infile,outfile):
    data = open(infile, "r").read()
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    with open(outfile, "w") as fp:
        fp.write(decode)

#rle_encode("./resultados\\bible_BWT.txt", "./resultados\\bible_BWT_RLE.bin")
rle_encode("./dataset\\finance.csv", "./resultados\\finance_RLE.bin")
rle_encode("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_RLE.bin")
rle_encode("./dataset\\random.txt", "./resultados\\random_RLE.bin")
