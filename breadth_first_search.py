from collections import deque
graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","johnny M"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"]=[]
graph["johnny"] = []
print(graph)

def person_is_seller(person):
    return person[-1] == "M"
def bfs(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        print(search_queue)
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person[:-1].title()+"is a Mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
        else:
            print(f"{person} is already searched!")
    return False
print(bfs(graph,"you"))



