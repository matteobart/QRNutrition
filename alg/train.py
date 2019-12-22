import huffman 

input_files = ['../nutritionV1.json']
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

print("Letter Frequencies")
forHuff = []
for k, v in reversed(sorted(letter_freq.items(), key=lambda item: item[1])):
	print(k, v)
	forHuff.append((k, v))

h = huffman.Huffman(forHuff)
h.print()
print(h.getPaths())







