graph = {} 
nodes=input("Name the nodes:\n").replace(""," ").replace(","," ").split()
start=input("Define your start Node:\n")
end=nodes.pop(nodes.index(input("Define your finish Node:\n")))
for node in nodes:
    graph[node]={} 
    neighbors=input(f"Neighbors of {node}:\n").replace(""," ").replace(","," ").split()
    for neighbor in neighbors :
        graph[node][neighbor]= int(input(f"Cost {node} -> {neighbor}:\n"))
graph[end]=None
print(graph)
costs = {node: graph[start][node] if node in graph[start] else float("inf") 
	 for node in graph.keys() 
	 if node != start}
parents = {node: start for node in graph[start].keys()}
