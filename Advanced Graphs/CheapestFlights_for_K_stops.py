class Solution:
	def findCheapestPrice(self, n, flights, src, dst, k):
		prices = [float("inf")] *n
		prices[src] = 0
		for i in range(k+1):
			tmpPrices = prices.copy()
			for s, d, p in flights: # s = source, d = destination, p = price
				if prices[s] == float("inf"):
					continue
				if prices[s] + p < tmpPrices[d]:
					tmpPrices[d] = prices[s] + p
			prices = tmpPrices
		return -1 if prices[dst] == float('inf') else prices[dst]
if __name__ == '__main__':
	s = Solution()
	n = 4
	flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] 
	src = 0
	dst = 3
	k = 1	
	result = s.findCheapestPrice(n, flights, src, dst, k)
	print(f"Output: {result}")
