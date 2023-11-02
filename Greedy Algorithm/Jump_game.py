class Solution:
    def canJump(self, nums):
        goal = len(nums) -1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

s = Solution()
array = [2,3,1,1,4]
result = s.canJump(array)
print(result)
