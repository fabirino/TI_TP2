import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy.io import wavfile
import math
# import huffmancodec

P = [0, 3, 0, 1, 0, 3, 0, 0, 1]
a = [0, 1, 2, 3]
alfabetoenglish = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabetocolors = [i for i in range(256)]

# Exercicio 1----------------------------------------------------------------------

def mostra_histograma(a, ocorrencias, nome = "Histograma"):
    plt.title(nome)
    plt.bar(a, ocorrencias, color="#117874")
    plt.xlabel("Alfabeto")
    plt.ylabel("Ocorrencias")
    # plt.grid(True)
    plt.show()


def calcula_ocorrencias(P, alfabeto): 
    dic = {}
    ocorrencias = []
    for i in alfabeto:
        dic.setdefault(i, 0)
    for i in P:
        if(i in dic.keys()):
            dic[i] += 1
    for v in dic.values():
        ocorrencias.append(v)
    return ocorrencias


# Exercicio 2 ----------------------------------------------------------------------


def calcula_entropia(tabOcorrencias):
    entropia = 0
    ocorrencias = tabOcorrencias
    ocorrencias = np.copy(ocorrencias)
    ocorrencias = ocorrencias[ocorrencias != 0]
    soma = np.sum(ocorrencias)
    entropia = np.sum((ocorrencias/soma) * np.log2(ocorrencias/soma))
    return abs(entropia)


# Exercicio 3 ----------------------------------------------------------------------


kid = img.imread("./data\kid.bmp").flatten()
homer = img.imread("./data\homer.bmp").flatten()
homerbin = img.imread("./data\homerBin.bmp").flatten()

# # imagens
# print("A entropia da imagem \"homer\" é ", end="")
# mostra_histograma(alfabetocolors, calcula_ocorrencias(homer, alfabetocolors), "Homer")
# print(round(calcula_entropia(calcula_ocorrencias(homer, alfabetocolors)), 3))

# print("A entropia da imagem \"homerbin\" é ", end="")
# mostra_histograma(alfabetocolors,calcula_ocorrencias(homerbin,alfabetocolors), "Homerbin")
# print(round(calcula_entropia(calcula_ocorrencias(homerbin,alfabetocolors)),3))

# print("A entropia da imagem \"kid\" é ", end="")
# mostra_histograma(alfabetocolors,calcula_ocorrencias(kid,alfabetocolors), "Kid")
# print(round(calcula_entropia(calcula_ocorrencias(kid,alfabetocolors)),3))

[fs, guitar] = wavfile.read("./data\guitarSolo.wav")
# print("A entropia do som \"guitar\" é ", end="")
# mostra_histograma(alfabetocolors,calcula_ocorrencias(guitar,alfabetocolors), "Guitar")
# print(round(calcula_entropia(calcula_ocorrencias(guitar,alfabetocolors)),3))

ficheirotxt = open("./data\english.txt", 'r')
texto = ficheirotxt.read()
# print("A entropia do texto \"english.txt\" é ", end="")
# mostra_histograma(alfabetoenglish,calcula_ocorrencias(texto,alfabetoenglish), "Texto")
# print(round(calcula_entropia(calcula_ocorrencias(texto,alfabetoenglish)),3))
ficheirotxt.close()

# Exercicio 4 ----------------------------------------------------------------------

def tabela_probabilidade(P, symbols):
    tabela = []
    aux = calcula_ocorrencias(P, symbols)
    for i in aux:
        tabela.append(i/len(P))

    return tabela

def media(length, prob):
    media = 0
    for i in range(len(prob)):
        media += length[i]*prob[i]
    return media

def variancia(length,prob,media):
    var = 0
    for i in range(len(prob)):
        var += math.pow(length[i]-media,2) * prob[i]
    return var

# codec_homer = huffmancodec.HuffmanCodec.from_data(homer)
# symbols_homer, lengths_homer = codec_homer.get_code_len()
# print("A média de bits usados com a codificação huffman da imagem \"homer\" é ", end="")
# mediahomer = media(lengths_homer,tabela_probabilidade(homer,symbols_homer))
# print(mediahomer)
# print("A variancia de bits usados com a codificação huffman da imagem \"homer\" é ", end="")
# print(variancia(lengths_homer,tabela_probabilidade(homer,symbols_homer),mediahomer))
# ----------------------------------------------------------------------------------

# codec_homerbin = huffmancodec.HuffmanCodec.from_data(homerbin)
# symbols_homerbin, lengths_homerbin = codec_homerbin.get_code_len()
# print("A média de bits usados por símbolo com a codificação huffman da imagem \"homerbin\" é ", end="")
# mediahomerbin = media(lengths_homerbin,tabela_probabilidade(homerbin,symbols_homerbin))
# print(mediahomerbin)
# print("A variancia de bits usados com a codificação huffman da imagem \"homerbin\" é ", end="")
# print(variancia(lengths_homerbin,tabela_probabilidade(homerbin,symbols_homerbin),mediahomerbin))

# ----------------------------------------------------------------------------------

# codec_kid = huffmancodec.HuffmanCodec.from_data(kid)
# symbols_kid, lengths_kid = codec_kid.get_code_len()
# print("A média de bits usados por símbolo com a codificação huffman da imagem \"kid\" é ", end="")
# mediakid = media(lengths_kid,tabela_probabilidade(kid,symbols_kid))
# print(mediakid)
# print("A variancia de bits usados com a codificação huffman da imagem \"kid\" é ", end="")
# print(variancia(lengths_kid,tabela_probabilidade(kid,symbols_kid),mediakid))

# ----------------------------------------------------------------------------------

# codec_guitar = huffmancodec.HuffmanCodec.from_data(guitar)
# symbols_guitar, lengths_guitar = codec_guitar.get_code_len()
# print("A média de bits usados por símbolo com a codificação huffman do som \"guitar\" é ", end="")
# mediaguitar = media(lengths_guitar,tabela_probabilidade(guitar,symbols_guitar))
# print(mediaguitar)
# print("A variancia de bits usados com a codificação huffman da imagem \"guitar\" é ", end="")
# print(variancia(lengths_guitar,tabela_probabilidade(guitar,symbols_guitar),mediaguitar))

# ----------------------------------------------------------------------------------

# codec_texto = huffmancodec.HuffmanCodec.from_data(texto)
# symbols_texto, lengths_texto = codec_texto.get_code_len()
# print("A média de bits por símbolo usados com a codificação huffman do texto \"homer\" é ", end="")
# mediatexto = media(lengths_texto,tabela_probabilidade(texto,symbols_texto))
# print(mediatexto)
# print("A variancia de bits usados com a codificação huffman da imagem \"texto\" é ", end="")
# print(variancia(lengths_texto,tabela_probabilidade(texto,symbols_texto),mediatexto))

# Exercicio 5-----------------------------------------------------------------------

def ocorrencia(P):  
    dic = {}
    for i in range(0,len(P),2):
        aux = (P[i],P[i+1])
        if(aux not in dic.keys()):
            dic.setdefault(aux, 1)
        else:
            dic[aux] += 1
    ocorrencias = []
    keys = []
    for v in dic.values():
        ocorrencias.append(v)
    for i in dic.keys():
        aux = str(i)
        keys.append(aux)
    mostra_histograma(keys,ocorrencias)
    return ocorrencias

# print("A entropia da imagem \"homer\" quando se agrupam 2 simbolos de cada vez é ", end="")
# print((calcula_entropia(ocorrencia(homer)))/2)

# print("A entropia da imagem \"homerbin\" quando se agrupam 2 simbolos de cada vez é ", end="")
# print((calcula_entropia(ocorrencia(homerbin)))/2)

# print("A entropia da imagem \"kid\" quando se agrupam 2 simbolos de cada vez é ", end="")
# print((calcula_entropia(ocorrencia(kid)))/2)

# print("A entropia do som \"guitar\" quando se agrupam 2 simbolos de cada vez é ", end="")
# print((calcula_entropia(ocorrencia(guitar)))/2)

# print("A entropia do texto \"english.txt\" quando se agrupam 2 simbolos de cada vez é ", end="")
# print((calcula_entropia(ocorrencia(texto)))/2)


# Exercicio 6-----------------------------------------------------------------------

query = [2, 6, 4, 10, 5, 9, 5, 8, 0, 8]
target = [6, 8, 9, 7, 2, 4, 9, 9, 4, 9, 1, 4, 8, 0, 1, 2, 2, 6, 3, 2, 0, 7, 4, 9,
          5, 4, 8, 5, 2, 7, 8, 0, 7, 4, 8, 5, 7, 4, 3, 2, 2, 7, 3, 5, 2, 7, 4, 9, 9, 6]

def informacaomutua(query, target, passo):
    infoMutua = []
    index = 0
    dic = {}
    H_X = calcula_entropia(calcula_ocorrencias(query, np.unique(query)))
    while (index+len(query) <= len(target)):
        aux = target[index: index + len(query)]
        H_Y = calcula_entropia(calcula_ocorrencias(aux, np.unique(aux)))
        dic = {}
        ocorrencias = []
        for i in range(len(query)):
            tup = (query[i], aux[i])
            if(tup in dic.keys()):
                dic[tup] += 1
            else:
                dic.setdefault(tup, 1)
        for v in dic.values():
            ocorrencias.append(v)
        H_XY = calcula_entropia(ocorrencias)
        I = H_X + H_Y - H_XY
        infoMutua.append(round(I, 4))
        index += passo
    return infoMutua

# print(informacaomutua(query,target,1))

# Exercicio 6. b)--------------------------------------------------------------------


[fsguitar, dataguitar] = wavfile.read('./data\\guitarSolo.wav')
[fstarget01, datatarget01] = wavfile.read('./data\\target01 - repeat.wav')
[fstarget02, datatarget02] = wavfile.read('./data\\target02 - repeatNoise.wav')

# infomutua01 = informacaomutua(dataguitar,datatarget01,(int)(len(dataguitar)/4))
# print(infomutua01)
# infomutua02 = informacaomutua(dataguitar,datatarget02,(int)(len(dataguitar)/4))
# print(infomutua02)

# plt.figure(0)
# plt.subplot(211)
# plt.plot(np.arange(len(infomutua01)),infomutua01)
# plt.subplot(212)
# plt.plot(np.arange(len(infomutua02)),infomutua02)
# plt.show()


# Exercicio 6c)----------------------------------------------------------------------
# [fsSong01, dataSong01] = wavfile.read('./data\\Song01.wav')
# [fsSong02, dataSong02] = wavfile.read('./data\\Song02.wav')
# [fsSong03, dataSong03] = wavfile.read('./data\\Song03.wav')
# [fsSong04, dataSong04] = wavfile.read('./data\\Song04.wav')
# [fsSong05, dataSong05] = wavfile.read('./data\\Song05.wav')
# [fsSong06, dataSong06] = wavfile.read('./data\\Song06.wav')
# [fsSong07, dataSong07] = wavfile.read('./data\\Song07.wav')

# dicsongs = {}

# infoMutuaSong01 = informacaomutua(dataguitar, dataSong01, (int)(len(dataguitar)/4))
# print("infoMutua01 " , infoMutuaSong01)
# ISong01 = np.max(infoMutuaSong01)
# dicsongs.setdefault("song01", ISong01)
# plt.title("song01")
# plt.plot(np.arange(len(infoMutuaSong01)), infoMutuaSong01)
# plt.show()


# infoMutuaSong02 = informacaomutua(dataguitar, dataSong02, (int)(len(dataguitar)/4))
# print("infoMutua02 " ,infoMutuaSong02)
# ISong02 = np.max(infoMutuaSong02)
# dicsongs.setdefault("song02", ISong02)
# plt.title("song02")
# plt.plot(np.arange(len(infoMutuaSong02)), infoMutuaSong02, marker="x")
# plt.show()


# infoMutuaSong03 = informacaomutua(dataguitar, dataSong03, (int)(len(dataguitar)/4))
# print("infoMutua03 " ,infoMutuaSong03)
# ISong03 = np.max(infoMutuaSong03)
# dicsongs.setdefault("song03", ISong03)
# plt.title("song03")
# plt.plot(np.arange(len(infoMutuaSong03)), infoMutuaSong03)
# plt.show()

# infoMutuaSong04 = informacaomutua(dataguitar, dataSong04, (int)(len(dataguitar)/4))
# print("infoMutua04 " ,infoMutuaSong04)
# ISong04 = np.max(infoMutuaSong04)
# dicsongs.setdefault("song04", ISong04)
# plt.title("song04")
# plt.plot(np.arange(len(infoMutuaSong04)), infoMutuaSong04)
# plt.show()

# infoMutuaSong05 = informacaomutua(dataguitar, dataSong05, (int)(len(dataguitar)/4))
# print("infoMutua05 " ,infoMutuaSong05)
# ISong05 = np.max(infoMutuaSong05)
# dicsongs.setdefault("song05", ISong05)
# plt.title("song05")
# plt.plot(np.arange(len(infoMutuaSong05)), infoMutuaSong05)
# plt.show()

# infoMutuaSong06 = informacaomutua(dataguitar, dataSong06, (int)(len(dataguitar)/4))
# print("infoMutua06 " ,infoMutuaSong06)
# ISong06 = np.max(infoMutuaSong06)
# dicsongs.setdefault("song06", ISong06)
# plt.title("song06")
# plt.plot(np.arange(len(infoMutuaSong06)), infoMutuaSong06)
# plt.show()

# infoMutuaSong07 = informacaomutua(dataguitar, dataSong07, (int)(len(dataguitar)/4))
# print("infoMutua07 " ,infoMutuaSong07)
# ISong07 = np.max(infoMutuaSong07)
# dicsongs.setdefault("song07", ISong07)
# plt.title("song07")
# plt.plot(np.arange(len(infoMutuaSong07)), infoMutuaSong07)
# plt.show()

# valor = []
# for i in dicsongs.values():
#     valor.append(i)
# valor.sort(reverse=True)
# for i in valor:
#     for k in dicsongs.keys():
#         if(dicsongs[k] == i):
#             print(k, "--->", i)
