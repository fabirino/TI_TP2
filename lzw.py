# https://github.com/amycardoso/lzw-text-file-compression/blob/master/lzw.py

import pickle

# função que realiza a compressao da entrada
def compressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}  # armazena o dicionário
    resultado = []  # armazena o resultado comprimido
    temp = ""  # variável que irá armazenar as substrings

    # Adicionando tabela ASCII ao dicionário
    for i in range(0, tamanhoDicionario):
        dicionario[str(chr(i))] = i  # Como fica o dicionário {'a': 97, 'b': 98}
    # assim podemos percorrer o arquivo, e substituir as substrings por seus respectivos inteiros

    for c in entrada:  # Percorre o arquivo
        temp2 = temp + str(c) # temp2 recebe o caractere atual mais o anterior para verificar se existe no dicionário
        if temp2 in dicionario.keys():  # se estiver no dicionário temp = temp2 para ser concatenado posteriormente com o próximo caractere
            temp = temp2
        else:  # caso o conteúdo de temp2 não esteja no dicionário
            resultado.append(dicionario[
                                 temp])  # pegamos o inteiro que representa a string anterior no dicionário e adicionamos ao resultado
            dicionario[temp2] = tamanhoDicionario  # em seguida adicionamos temp2 ao dicionário
            tamanhoDicionario += 1  # incrementa tamanho do dicionário
            temp = "" + str(c)  # reseta a variável com a substring atual

    if temp != "":  # caso a string temporária não esteja vazia, deve-se adicionar ao resultado
        resultado.append(dicionario[temp])  # pegando o inteiro que a representa no dicionário

    return resultado


# função que realiza a descompressao da entrada
def descompressao(entrada):
    tamanhoDicionario = 256
    dicionario = {}  # armazena o dicionário
    resultado = []  # armazena o resultado descomprimido

    # inicializando dicionário com tabela ASCII
    for i in range(0, tamanhoDicionario):
        dicionario[i] = str(
            chr(i))  # Como o dicionário fica, ex: {97: 'a', 98: 'b'}, diferente do dicionário de compressão

    anterior = chr(
        entrada[0])  # pega o primeiro caractere e marca como anterior, por exemplo: chr(97) retorna a string 'a'
    entrada = entrada[1:]  # remove o primeiro caractere da entrada
    resultado.append(anterior)  # adiciona o primeiro caractere ao resultado

    for bit in entrada:
        aux = ""
        if bit in dicionario.keys():
            aux = dicionario[bit]  # pega o caractere correspondente ao bit no dicionário
        else:  # Quando o bit não ta no dicionário, deve se pegar
            aux = anterior + anterior[
                0]  # o ultimo caractere impresso + a primeira posição do último caractere impresso
            # pois devemos decodificar bits que não estão presentes no dicionário, então temos que adivinhar o que ele representa, por exemplo:
            # digamos que o bit 37768 não ta no dicionário, então pegamos o último caractere impresso, por exemplo foi 'uh'
            # e pegamos ele 'uh' mais sua primeira posição 'u', resultando em 'uhu', que é a representação do bit 37768
            # o único caso em que isso pode ocorrer é se a substring começar e terminar com o mesmo caractere ("uhuhu").

        resultado.append(aux)  # adiciona ao resultado
        # Resimulando como as substrings foram adicionadas durante a compressão
        dicionario[tamanhoDicionario] = anterior + aux[
            0]  # adiciona ao dicionário o caractere anterior mais a primeira posição do caractere atual
        tamanhoDicionario += 1  # incrementa tamanho do dicionário
        anterior = aux  # anterior recebe o caractere atual
    return resultado

entrada = open( "./dataset\\bible.txt", "r").read()
saida = open("./resultados\\biblelzw.bin", "wb")
comprimido = compressao(entrada)
pickle.dump(comprimido, saida)  # escreve no arquivo binário a compressão
# dump salva o conteúdo serializado do objeto nesse arquivo
entrada = pickle.load(open("./resultados\\biblelzw.bin", "rb"))
saida = open("./resultados\\decoderbiblelzw.txt", "w")

descomprimido = descompressao(entrada)
for l in descomprimido:  # grava no arquivo o resultado da descompressão
    saida.write(l)
saida.close()
