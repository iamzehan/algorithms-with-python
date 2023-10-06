def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digitsToChar = { 
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
        }
    def backtrack(i, res, currStr):
        if len(currStr)==len(digits):
            res.append(currStr)
            return 
        for c in digitsToChar[digits[i]]:
            backtrack(i+1, res, currStr+c)
        return res
    
    if digits:
        return backtrack(0, [], "")
    else:
        return []
