# Greedy algorithms to find the best stations for maximum coverage
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"]) # This tells us which states we need to cover
stations = {}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"]=set(["wa","id","mt"])
stations["kthree"]=set(["or","nv","ca"])
stations["kfour"]=set(["nv","ut"])
stations["kfive"]=set(["ca","az"])
final_stations = set() #final result of selected stations
while states_needed:
    best_station=None # initially we assume there are no best stations, so we loop through all of them 
    states_covered=set() # this keeps the covered stations in check while going through all the stations
    for station, states in stations.items():
        covered = states_needed & states # finding the common values among the states needed and the states that are covered 
        if len(covered)> len(states_covered): # if the covered states in the current station, covers more states than the states that are covered
            states_covered = covered # then we update the states covered with this value
            best_station = station  # then we are safe to say, this is the best station for our maximum coverage
    final_stations.add(best_station) # then we add the best station to our final selection
    states_needed -= states_covered # then we get rid of the states that are already covered

print(final_stations)
