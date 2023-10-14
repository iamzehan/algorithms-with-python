"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""

class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True
        
    def search(self, word):

        def dfs(i,root):
            current = root
            for i in range(i,len(word)):
                if word[i] == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                if word[i] not in current.children:
                    return False
                current=current.children[word[i]]
            return current.isWord
            
        return dfs(0, self.root)

obj = WordDictionary()
param1=["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
param2=[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
output = [] 
operations={ 
			"WordDictionary":None, 
			"addWord": obj.addWord, 
			"search": obj.search
			} 
for i in range(len(param1)): 
	method = operations[param1[i]] 
	if method is not None: 
		output.append(method(param2[i][0])) 
	else: 
		output.append(None) 
print(output)

# >> [None, None, None, None, False, True, True, True] 
