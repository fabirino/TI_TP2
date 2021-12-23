## Compressão (e descompressão) Lossless de ficheiros de texto

O código é constituído por um ficheiro main.py e vários ficheiros auxiliares, cada um deles contendo as funções de um método de compressão ou de codificação. De notar que os ***ficheiros auxiliares contêm código de outros autores*** adaptado por nós. Ao correr o ficheiro main, o utilizador depara-se com uma interface na consola onde pode escolher o método de compressão que pretende utilizar. O programa chama então as funções de compressão e de descompressão do ficheiro do método correspondente e no final é mostrado o tempo de compressão de cada ficheiro bem como o tamanho do ficheiro final e o rácio de compressão.

## Estrutura do projeto

A pasta contém pastas que permitem a organização dos ficheiros de código, de texto ou binários, onde:

- `dataset`: pasta que contém os ficheiros de texto originais a serem comprimidos
- `resultados`: pasta que guarda os ficheiros de texto após compressão
- `decompress`: pasta que contém a descompressão dos ficheiros previamente comprimidos

Cada ficheiro dentro dentro de alguma destas pastas tem o nome original, porém se tiver um sufixo significa que foi aplicada a compressão do sufixo correspondeste e se tiver o prefixo "decoder_" significa que o ficheiro foi descomprimido.


Fora destas pastas encontram-se os ficheiros "*.py" :

- `main.py`: ficheiro que contém a aplicação proprimante dita, onde é possivel escolher que metodo(s) de compressão se pretendem aplicar
- `RESTANTES`: ficheiros auxilares que contém o código de leitura, escrita, compressão e descompressão segundo o método correspondente a esse ficheiro.

### IMPORTANTE

Para correr o código do PPM é necessário instalar uma biblioteca que permite este tipo de codificação
Para isso corre o seguinte programa no terminal

- pip install ppmd-cffi