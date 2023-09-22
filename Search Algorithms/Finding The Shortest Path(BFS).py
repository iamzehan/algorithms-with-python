import pprint
def buildGraph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge
        if a not in graph.keys():
            graph[a]=[]
        if b not in graph.keys():
            graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set([nodeA])
    queue = [[nodeA,0]]
    
    while len(queue)>0:
        [node, distance] = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor,distance+1])
    return -1

if __name__ == '__main__':
    edges = [
      ['w', 'x'],
      ['x', 'y'],
      ['z', 'y'],
      ['z', 'v'],
      ['w', 'v']
    ]
    pprint.pprint(shortestPath(edges, 'w', 'z'))
    edges = [
      ['w', 'x'],
      ['x', 'y'],
      ['z', 'y'],
      ['z', 'v'],
      ['w', 'v']
    ]
    pprint.pprint(shortestPath(edges, 'y', 'x'))
    edges = [
      ['a', 'c'],
      ['a', 'b'],
      ['c', 'b'],
      ['c', 'd'],
      ['b', 'd'],
      ['e', 'd'],
      ['g', 'f']
    ]
    pprint.pprint(shortestPath(edges, 'a', 'e'))
    
