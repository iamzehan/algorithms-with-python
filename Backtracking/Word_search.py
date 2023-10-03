"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

| A | B | C | E |
| S | F | C | S |
| A | D | E | E |

word = | A | B | C | C | E | D |
"""
def word_search(grid:list[list[str]],word:str)->bool:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(r, c,0):
                return True
    return False

def explore(r:int, c:int, i:int, visited=set())->bool:
    #taking the current position
    pos = (r,c)
    # checking the bounds
    rowInbounds = 0<=r and r<len(grid)
    colInbounds = 0<=c and c<len(grid[0])
    
    #if we have reached the length of the word 
    if i == len(word):
        return True
    #checking all aspects of base case
    if (not rowInbounds or not colInbounds
    or grid[r][c] !=word[i] or pos in visited):
        return False
    # push the position into visited
    visited.add(pos)
    result = (
        explore(r-1,c, i+1, visited) or  # up
        explore(r+1, c, i+1, visited) or # down
        explore(r, c-1, i+1, visited) or # left
        explore(r, c+1, i+1, visited)    # right
        )
    #remove from the top of the stack
    visited.remove(pos) 
    
    return result
    
if __name__ == '__main__':
    #global
    grid = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
    word = "ABCCED"
    
    if not word_search(grid, word):
        print(f"Couldn't find \"{word}\"")
    else:
        print(f"\"{word}\" Found!")
