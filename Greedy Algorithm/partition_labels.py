class Solution:
    def partitionLabels(self, s):
        lastIndex = {v:i for i, v in enumerate(s)}
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(size)
                size = 0
        return res    

if __name__ == '__main__':
    solution = Solution()
    s = "ababcbacadefegdehijhklij"
    result = solution.partitionLabels(s)
    print(result)
