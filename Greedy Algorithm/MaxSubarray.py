class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum+=n
            if curSum>maxSub:
                maxSub = curSum
        return maxSub

s = Solution()
array = [-2,1,-3,4,-1,2,1,-5,4]
result = s.maxSubArray(array)
print(result)
