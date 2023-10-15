"""
Problem:
________
Find given words 
"oath","pea","eat","rain"
from the following grid

| o | a | a | n |
| e | t | a | e |
| i | h | k | r |
| i | f | l | v |

Once you find a word you have to add it to a list
that list would be your final output
"""

class TrieNode():
	def __init__(self):
		self.children = {}
		self.isWord = False
	def addWord(self, word):
		cur = self
		for c in word: 
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		cur.isWord = True
class WordSearch(object):
	def findWords(self, board, words):
		root = TrieNode()
		for word in words:
			root.addWord(word)
		ROWS, COLS = len(board),len(board[0])
		res, visited = set(), set()
		def dfs(r, c, node, word):
			if(r<0 or c<0 or
	        c == COLS or
	        r == ROWS or
	        board[r][c] not in node.children):
				return 
            
			node = node.children[board[r][c]]
			word += board[r][c]
			temp, board[r][c] = board[r][c], 0 
			# if current node isWord then we add it to the result
			if node.isWord == True:
				res.add(word)
			dfs(r-1,c, node, word) #down
			dfs(r+1,c, node, word) #up
			dfs(r,c+1, node, word) #right
			dfs(r,c-1, node, word) #left
			board[r][c] = temp
		for r in range(ROWS):
			for c in range(COLS):
				dfs(r,c,root,"")
				
		
		return list(res)	

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
words = ["oath","pea","eat","rain"]
obj = WordSearch()
print(obj.findWords(board, words))
# >> ['oath', 'eat'] 
