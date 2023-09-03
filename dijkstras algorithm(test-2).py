graph = {}
graph["A"] = {}
graph["A"]["B"] = 4
graph["A"]["C"] = 5
graph["B"]={}
graph["B"]["D"] = 9
graph["B"]["C"] = 11
graph["B"]["E"] = 7
graph["C"]={}
graph["C"]["B"] = 11
graph["C"]["E"] = 3
graph["D"]={}
graph["D"]["E"] = 13
graph["D"]["F"] = 2
graph["E"] = {}
graph["E"]["D"] = 13
graph["E"]["F"] = 6
graph["F"] = None

costs = {}
costs["B"] = 4
costs["C"] = 5
costs["D"] = float("inf")
costs["E"] = float("inf")
costs["F"] = float("inf")

parents={}
parents["B"] = "A"
parents["C"] = "A"

def find_lowest_cost_node(costs,processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def find_path(tree, start_node, end_node):
    path = []
    current_node = end_node
    
    while current_node != start_node:
        path.append(current_node)
        if current_node not in tree:
            print("No path found")
            return
        current_node = tree[current_node]
    
    path.append(start_node)
    return "Path:", " -> ".join(path[::-1])
    
def dijkstras_algorithm(graph,costs,parents,start,end):
    cost=0
    processed = []
    node = find_lowest_cost_node(costs,processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        if neighbors != None:
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n]>new_cost:
                    costs[n] = new_cost
                    parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs,processed)
    
    return costs,find_path(parents,start,end)
start = "A"
end = "F"
lowest_costs, lowest_cost_path = dijkstras_algorithm(graph,costs,parents,start, end)

print(f"The lowest cost to get to all the nodes from {start} are:\n")
for k, v in lowest_costs.items():
    print(f"{start} => {k} ------- {v}")
print("\n")

print(f"The lowest cost path from {start} to {end} is:\n {lowest_cost_path}")

            
        
