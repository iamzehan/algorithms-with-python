graph = {} 
nodes=list(input("What are the name of the Nodes?\n"))

for i in nodes[:-1]:
    graph[i]={} 
    neighbors=list(input(f"Neighbors of {i}:\n"))
    for j in neighbors :
        graph[i][j]= int(input(f"Cost {i} -> {j}:\n"))
graph[nodes[-1]]=None
print(graph)
       
