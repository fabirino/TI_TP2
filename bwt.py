# https://stackoverflow.com/questions/21297887/performance-issues-in-burrows-wheeler-in-python
import time
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

def allBWT():
    print("Comprimindo \'bible.txt\'...")
    tempo = time.time()
    encodeFile("./dataset\\bible.txt", "./resultados\\bible_BWT.txt")
    tempo = time.time() - tempo
    print(f"Tempo de compressao -> {round(tempo, 4)} segundos")
    print("Ficheiro \'bible.txt\' comprimido com BWT")
    print("----------------------------------------------------------------")

    print("Comprimindo \'finance.csv\'...")
    tempo2 = time.time()
    encodeFile("./dataset\\finance.csv", "./resultados\\finance_BWT.txt")
    tempo2 = time.time() - tempo2
    print(f"Tempo de compressao -> {round(tempo2, 4)} segundos")
    print("Ficheiro \'finance.csv\' comprimido com BWT")
    print("----------------------------------------------------------------")

    print("Comprimindo \'jquery-3.6.0.js\'...")
    tempo3 = time.time()
    encodeFile("./dataset\\jquery-3.6.0.js", "./resultados\\jquery-3.6.0_BWT.txt")
    tempo3 = time.time() - tempo3
    print(f"Tempo de compressao -> {round(tempo3, 4)} segundos")
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com BWT")
    print("----------------------------------------------------------------")
    
    print("Comprimindo \'random.txt\'...")
    tempo4 = time.time()
    encodeFile("./dataset\\random.txt", "./resultados\\random_BWT.txt")
    tempo4 = time.time() - tempo4
    print(f"Tempo de compressao -> {round(tempo4, 4)} segundos")
    print("Ficheiro \'random.txt\' comprimido com BWT")
    print("----------------------------------------------------------------")
    print()
