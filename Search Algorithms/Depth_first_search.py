def dfs(data, start, visited=set(), output=[]):
    if start not in visited:
        output.append(start)
    
    visited.add(start)
    # take those neighbors except for the visited ones
    for i in sorted(list(data[start]-visited)):
        #let's go deep inside until we have none left
        dfs(data, i, visited)
    return " ".join(output)

# sample data in dictionary form
data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
        }


if __name__ == '__main__':
    print(dfs(data, 'D'))
