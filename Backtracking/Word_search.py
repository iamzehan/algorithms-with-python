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

def explore(r:int, c:int, i:int)->bool:
    if i==len(word):
        return True
    if (
        r < 0 or r >= len(grid) or 
        c < 0 or c >= len(grid[0]) or 
        grid[r][c] != word[i]
        ):
        return False
    
    temp, grid[r][c] = grid[r][c], "*"
    
    if(explore(r-1, c, i+1) or
        explore(r+1, c, i+1) or
        explore(r, c-1, i+1) or
        explore(r, c+1, i+1)):
        return True
    grid[r][c]=temp
    return False
    
    
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
