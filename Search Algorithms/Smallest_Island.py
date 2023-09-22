def smallest_island(grid):
    visited = set()
    min_size= float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size =explore_size(grid, r, c,visited)
            if size>0 and size<min_size:
                min_size=size
    if min_size==float("inf"):
        return "No Islands found"
    return min_size

def explore_size(grid, r, c, visited):
    rowInbounds = 0<r and r<len(grid)
    colInbounds = 0<c and c<len(grid[0])
    if (not rowInbounds or not colInbounds):
        return 0
    if grid[r][c] == 'W':
        return 0 
    pos = f"{r},{c}"
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1
    size += explore_size(grid, r-1,c, visited)
    size += explore_size(grid, r+1,c, visited)
    size += explore_size(grid, r,c-1, visited)
    size += explore_size(grid, r,c+1, visited)
    
    return size
if __name__ == '__main__':
    grid = [
      ['W', 'L', 'W', 'W', 'W'],
      ['W', 'L', 'W', 'W', 'W'],
      ['W', 'W', 'W', 'L', 'W'],
      ['W', 'W', 'L', 'L', 'W'],
      ['L', 'W', 'W', 'L', 'L'],
      ['L', 'L', 'W', 'W', 'W'],
    ]
    print(smallest_island(grid))
    grid = [
      ['L', 'L', 'L'],
      ['L', 'L', 'L'],
      ['L', 'L', 'L'],
    ]
    print(smallest_island(grid))
    grid = [
      ['W', 'W'],
      ['W', 'W'],
      ['W', 'W'],
    ]
    print(smallest_island(grid))
