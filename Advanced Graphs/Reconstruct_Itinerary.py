class Solution:
    def findItinerary(self, tickets):
        adj = {start: [] for start, destination in tickets}
        tickets.sort()
        for start, destination in tickets:
            adj[start].append(destination)
        res = ["JFK"]
        def dfs(start):
            if len(res) == len(tickets)+1:
                return True 
            if start not in adj:
                return False 
            temp = list(adj[start])
            for index, value in enumerate(temp):
                res.append(value)
                adj[start].pop(index)
                if dfs(value): return True
                res.pop()
                adj[start].insert(index, value)
            return False
        dfs("JFK")
        return res

if __name__ == '__main__':
    s = Solution()
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(s.findItinerary(tickets))
