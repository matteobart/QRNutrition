from heapq import * 
class Node:
	def __init__ (self, val):
		self.val = val
	def __lt__(self, other):
		return self.val < other.val 
    	# return comparison
	def __eq__(self, other):
		return self.val == other.val 
		# return comparison

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
			self.children[i].print(str(i) + path)

	def getPaths(self, path):
		ret = []
		for i in range(len(self.children)):
			ret += self.children[i].getPaths(str(i) + path)
		return ret

class Huffman:
	# [(h, 4), (q, 17), (r, 19)] 
	def __init__(self, tupleList):
		heap = []
		for tup in tupleList:
			key = tup[0]
			freq = tup[1]
			leaf = LeafNode(key, freq)
			heappush(heap, leaf)

		while (len(heap) > 1):
			pushUsTogether = []
			val = 0
			for _ in range(9):
				if len(heap) != 0:
					popped = heap.pop(0)
					pushUsTogether.append(popped)
					val += popped.val
			internal = InternalNode(val, pushUsTogether)
			heappush(heap, internal)
		self.root = heap[0]

	def print(self):
		self.root.print("")

	def getPaths(self):
		return self.root.getPaths("")


