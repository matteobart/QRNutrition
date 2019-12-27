import huffman 

default_input_files = ["nutritionV1.json", "nutritionV2.json"]

#will return a list of tuples 
#eg. [(char_str, int_str), ('y', '50'), ('}', 651)]
def get_encoding(input_files=default_input_files, debug_output=False):
    letter_freq = {}
    for input_file_name in input_files:
        f = open(input_file_name, "r")
        lines = f.readlines()
        for line in lines:
            for char in line:
                val = letter_freq.get(char)
                if val != None:
                    letter_freq[char] = val + 1
                else:
                    letter_freq[char] = 1
    if debug_output:
        print("Letter Frequencies")
    forHuff = [] #list of tuples in form (char: str, frequency: int)
    for k, v in reversed(sorted(letter_freq.items(), key=lambda item: item[1])):
        if debug_output:
            print(k, v)
        forHuff.append((k, v))

    h = huffman.Huffman(forHuff)
    return h.getPaths()


def encode(str, encoding=get_encoding(), strip_str=False):
    if strip_str:
        str = str.replace("\n", "").replace("\t", "")
    dict = {}
    for encode in encoding:
        dict[encode[0]] = encode[1]

    encoded_string = ""
    for char in str:
        encoded_string += dict[char]
    return encoded_string

def decode(str, encoding=get_encoding()):
    dict = {}
    for encode in encoding:
        dict[encode[1]] = encode[0]

    decoded_string = ""
    key = ""
    for char in str:
        key += char
        if dict.get(key) != None:
            decoded_string += dict[key]
            key = "" 
    return decoded_string

