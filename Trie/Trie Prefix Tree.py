class TrieNode:
	def __init__(self):
		self.children = {}
		self.endOfWord = False
class Trie:
	def __init__(self):
		self.root = TrieNode()
	#insert
	def insert(self, word:str) -> None:
		#starting from the root
		current = self.root
		#for every character in the given word
		for c in word:
			#check if that character exists in the children
			if c not in current.children: # character doesn't exist
				current.children[c] = TrieNode() #add that character to node
			#character exists
			current = current.children[c] # skip it and move to the next child
		#after all of them are added, mark the end of the word as True
		current.endOfWord = True
	
	#search 	
	def search(self, word:str) -> bool:
		# starting from the root
		current = self.root
		# going through every character of the word
		for c in word:
			# check if character exists in the children
			if c not in current.children:
				return False # the character doesn't exist 
			#character exists
			current = current.children[c]  # skip it and move to the next child
		# if it reaches here word exists and that means it's True anyway.
		return current.endOfWord 
	
	def startsWith(self, prefix: str) -> bool:
		#start from the root
		current = self.root
		#for every character in the prefix
		for c in prefix:
			#if character is in children or not
			if c not in current.children:
				return False # not a prefix
			#move to the next child
			current = current.children[c]
		#if that for loop ends without returning that means we've checked all the characters
		return True

t = Trie()
t.insert("apple") 
print(t.search("apple")) # >> True
print(t.startsWith("app")) # >> True	
