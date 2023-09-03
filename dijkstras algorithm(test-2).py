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

def dijkstras_algorithm(graph,costs,parents):
  cost = 0
  processed = []
  node = find_lowest_cost_node(costs,processed)
  while node is not None:
    cost = costs[node]
    print("-------------------------")
    print(f"Node: {node} Cost:{cost}")
    print("-------------------------")
    neighbors = graph[node]
    print(f"neighbours of {node} are {neighbors}")
    if neighbors !=None:
      for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        print(costs)
        print(f"New cost to get to {node}=>{n}: {new_cost}")
        if new_cost < costs[n]:
          costs[n] = new_cost # update cost
          parents[n] = node # new node becomes new parent for this neighbor
          print(f"Parent of {n} is now {node}")
      print("\n")
    processed.append(node)
    node = find_lowest_cost_node(costs,processed)
  print("\n")
  print("Nodes Processed: ",processed)
  return costs

print("\n")
start_node = "A"
distances = dijkstras_algorithm(graph,costs,parents)
print("Shortest distances from node '{}' to all other nodes:".format(start_node))
for node, distance in distances.items():
    print("Node '{}' : Distance = {}".format(node, distance))
print(parents)
            
        
