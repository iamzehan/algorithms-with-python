graph = {} 
nodes=input("Name the nodes:").replace(""," ").replace(","," ").split()
end=nodes.pop(nodes.index(input("Define your finsh Node:\n")))
for node in nodes:
    graph[node]={} 
    neighbors=input(f"Neighbors of {nodes}:\n").replace(""," ").replace(","," ").split()
		for neighbor in neighbors :
        graph[node][neighbor]= int(input(f"Cost {node} -> {neighbor}:\n"))
graph[end]=None
print(graph)
       
