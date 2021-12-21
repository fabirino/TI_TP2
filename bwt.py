# https://stackoverflow.com/questions/21297887/performance-issues-in-burrows-wheeler-in-python

def burroughs_wheeler_custom(text):
    N = len(text)
    text2 = text * 2
    class K:
        def __init__(self, i):
            self.i = i
        def __lt__(a, b):
            i, j = a.i, b.i
            for k in range(N): # use `range()` in Python 3
                if text2[i+k] < text2[j+k]:
                    return True
                elif text2[i+k] > text2[j+k]:
                    return False
            return False # they're equal

    inorder = sorted(range(N), key=K)
    return "".join(text2[i+N-1] for i in inorder)

def encodeFile(infile, outfile):
	fi = open(infile, "r").read()
	bwttransform = burroughs_wheeler_custom(fi)
	fo = open(outfile, "w")
	fo.write(bwttransform)
	fo.close()

#encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
# encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
# encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")