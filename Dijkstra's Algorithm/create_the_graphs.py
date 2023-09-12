def lowest_cost_node(costs,processed):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs.keys():
		if costs[node]<lowest_cost and node not in processed:
			lowest_cost = costs[node]
			lowest_cost_node = node
	return lowest_cost_node
def find_path(tree, start, end):
	path = []
	current_node = end
	while current_node != start:
		path.append(current_node)
		if current_node not in tree:
			return 
		else:
			current_node = tree[current_node]
	path.append(start)
	return "->".join(path[::-1])
def dijkstras_algorithm(graph,costs,parents, start, end):
	processed=[]
	node = lowest_cost_node(costs,processed)
	while node is not None:
		cost = costs[node]
		neighbors = graph[node]
		for neighbor in neighbors.keys():
			new_cost = cost+neighbors[neighbor]
			if new_cost<costs[neighbor]:
				costs[neighbor] = new_cost
				parents[neighbor] = node
		processed.append(node)
		node = lowest_cost_node(costs,processed)
	return costs, find_path(parents, start, end)
if __name__ == "__main__":
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
	costs, path = dijkstras_algorithm(graph,costs,parents, start, end)
	print(costs+"\n"+path)
