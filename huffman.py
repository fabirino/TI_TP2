import heapq
import pickle

"""
author: Bhrigu Srivastava
website: https:bhrigu.me
"""


class HuffmanCoding:
    def __init__(self,file,infile, outfile,dicfile):
        self.dicfile = dicfile
        self.file = file
        self.infile = infile
        self.outfile = outfile
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        # defining comparators less_than and equals
        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if (other == None):
                return False
            if (not isinstance(other, HeapNode)):
                return False
            return self.freq == other.freq

    # functions for compression:

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if (root == None):
            return

        if (root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if (len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self):

        with open(self.file, 'r+') as file, open(self.infile, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
            a_file = open(self.dicfile, "wb")
            pickle.dump(self.reverse_mapping, a_file)

            a_file.close()

    """ functions for decompression: """

    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self):
        if(len(self.reverse_mapping) == 0):
            a_file = open(self.dicfile, "rb")
            self.reverse_mapping = pickle. load(a_file)

        with open(self.infile, 'rb') as file, open(self.outfile, 'w') as output:
            bit_string = ""

            byte = file.read(1)
            while (len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output.write(decompressed_text)


def Huffman():
    bible = HuffmanCoding("./dataset\\bible.txt","./resultados\\bible_Huff.bin","./decompress\\decoder_bible_Huff.txt","./dicionarios\\bible_Huff.bin")
    bible.compress()
    print("Ficheiro \'bible.txt\' comprimido com Huffman")
    bible.decompress()
    print("Ficheiro \'bible_Huff.bin\' descomprimido com Huffman")
    finance = HuffmanCoding("./dataset\\finance.csv","./resultados\\finance_Huff.bin","./decompress\\decoder_finance_Huff.txt","./dicionarios\\finance_Huff.bin")
    finance.compress()
    print("Ficheiro \'finance.csv\' comprimido com Huffman")
    finance.decompress()
    print("Ficheiro \'finance_Huff.bin\' descomprimido com Huffman")
    jquery = HuffmanCoding("./dataset\\jquery-3.6.0.js","./resultados\\jquery-3.6.0_Huff.bin","./decompress\\decoder_jquery-3.6.0_Huff.txt","./dicionarios\\jquery-3.6.0_Huff.bin")
    jquery.compress()
    print("Ficheiro \'jquery-3.6.0.js\' comprimido com Huffman")
    jquery.decompress()
    print("Ficheiro \'jquery-3.6.0_Huff.bin\' descomprimido com Huffman")
    random = HuffmanCoding("./dataset\\random.txt","./resultados\\random_Huff.bin","./decompress\\decoder_random_Huff.txt","./dicionarios\\random_Huff.bin")
    random.compress()
    print("Ficheiro \'random.txt\' comprimido com Huffman")
    random.decompress()
    print("Ficheiro \'random_Huff.bin\' descomprimido com Huffman")

# def Huffmanencode(file,outfile,dicfile):
#     x = HuffmanCoding(file,outfile,"",dicfile)
#     x.compress()
#     print("Ficheiro \'{file}\' comprimido com Huffman")

# def Huffmandecode(file,outfile,dicfile):
#     x = HuffmanCoding(file,"",outfile,dicfile)
#     x.decompress()
#     print("Ficheiro \'{file}\' descomprimido com Huffman")