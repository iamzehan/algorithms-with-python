import heapq
from collections import defaultdict 
class Twitter(object):
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -=1 
    def getNewsFeed(self, userId):
        res = [] 
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                idx = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][idx]
                minHeap.append([count,tweetId, followeeId, idx-1])
        heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            count,tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx>=0:
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx-1])
        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


obj = Twitter() 
param1 = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"] 

param2 = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
output = [] 
operations={
		   "Twitter":None,
		   "postTweet": obj.postTweet,
		   "getNewsFeed": obj.getNewsFeed,
		   "follow": obj.follow,
		   "unfollow": obj.unfollow
		   } 
for i in range(len(param1)): 
	method = operations[param1[i]]
	if method is not None:
	   if len(param2[i])>1:
	       output.append(method(param2[i][0],param2[i][1]))
	   else:
	       output.append(method(param2[i][0]))
	else: 
		output.append(None) 
print(output)
