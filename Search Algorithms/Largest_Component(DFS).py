def largestComponent(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph,node,visited)
        if size>longest:
            longest=size
    return longest

def exploreSize(graph, node, visited):
    if node in visited:
        return 0
    else:
        visited.add(node)
    
    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, int(neighbor), visited)
    return size

if __name__ == '__main__':
    graphs = [
    {
      0: ['8', '1', '5'],
      1: ['0'],
      5: ['0', '8'],
      8: ['0', '5'],
      2: ['3', '4'],
      3: ['2', '4'],
      4: ['3', '2']
    },
    {
      1: ['2'],
      2: ['1','8'],
      6: ['7'],
      9: ['8'],
      7: ['6', '8'],
      8: ['9', '7', '2']
    },
    {
      3: [],
      4: ['6'],
      6: ['4', '5', '7', '8'],
      8: ['6'],
      7: ['6'],
      5: ['6'],
      1: ['2'],
      2: ['1']
    }, {
      0: ['4','7'],
      1: [],
      2: [],
      3: ['6'],
      4: ['0'],
      6: ['3'],
      7: ['0'],
      8: []
    }
    ]

for graph in graphs:
    print(largestComponent(graph))
