from heapq import * 
# used by train, no need to call directly

class Node:
	def __init__ (self, val):
		self.val = val
	def __lt__(self, other):
		return self.val < other.val 
	def __eq__(self, other):
		return self.val == other.val 

class LeafNode(Node):
	def __init__(self, letter, val):
		self.letter = letter
		Node.__init__(self, val)
	
	def print(self, path):
		print("Letter:", self.letter, "Freq:", self.val, "Path:", path)

	def getPaths(self, path):
		return [(self.letter, path)] #only a list for easy adding 

class InternalNode(Node):
	def __init__(self, val, children):
		self.children = children
		Node.__init__(self, val)

	def print(self, path):
		print("Freq:", self.val, "Path:", path)
		for i in range(len(self.children)):
			self.children[i].print(path+str(i))

	def getPaths(self, path):
		ret = []
		for i in range(len(self.children)):
			ret += self.children[i].getPaths(path+str(i))
		return ret

class Huffman:
	#tupleList should be in form [(char: string, frequency: int), ...]
	#there is no need for the list to be in any particular order
	#eg. [('h', 4), ('q', 17), ('r', 19)] 
	def __init__(self, tupleList):
		heap = []
		for tup in tupleList:
			key = tup[0]
			freq = tup[1]
			leaf = LeafNode(key, freq)
			heappush(heap, leaf)

		while (len(heap) > 1):
			future_children = []
			val = 0
			for _ in range(9):
				if len(heap) != 0:
					popped = heap.pop(0)
					future_children.append(popped)
					val += popped.val
			internal = InternalNode(val, future_children)
			heappush(heap, internal)
		self.root = heap[0]

	def print(self):
		self.root.print("")

	def getPaths(self):
		return self.root.getPaths("")


