# algorithms-with-python
A brief look at algorithms with python

# Thinking of going back to the basics?

The struggle is real when it comes to the basics of coding. Sometimes, we forget the basics while working on the more advanced stuff.
Don't worry, I've got you, and you've got this too. Let's go through those hard-to-grasp, abstract problems that make your head scratch.
Let's buckle up and say: 

<h1 align="center"> <img src=https://media.tenor.com/Lrx2omjrmLwAAAAC/captain-america-i-can-do-this-all-day.gif"> </h1>

# Why look here?
Well they don't break down codes for you like this, do they? 

# code
```python:
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
            print(res)
            return 
        for c in digitsToChar[digits[i]]:
            backtrack(i+1, res, currStr+c)
        return res
    
    if digits:
        return backtrack(0, [], "")
    else:
        return []
print(letterCombinations("23"))
```
👇
```
backtrack("")
	#doesn't hit base case
	for c in "abc":
		c= "a"
		backtrack("a")
			# doesn't hit base case
			for c in "def":
				c = "d"
				backtrack("ad")
					#hits base case
					["ad"]  #res
					return 
				c="e"
				backtrack("ae")
					#hits base case
					["ad","ae"] #res
					return
				c="f"
				backtrack("af")
					#hits base case
					["ad","ae","af"] #res
					return
				#for loop ends
			return  ["ad","ae","af"] #res
		#------------------------ "a" done --------------------------
		c = "b"
		backtrack("b")
			#doesn't hit base case
			#for c in "def"
				c="d"
				backtrack("bd")
					#hits base case
					["ad","ae","af","bd"] #res
					return
				c="e"
				backtrack("be")
					#hits base case
					["ad","ae","af","bd","be"] #res
					return 
				c="f"
				backtrack("bf")
					#hits base case
					["ad","ae","af","bd","be","bf"] #res
					return
				#for loop ends
			return  ["ad","ae","af","bd","be","bf"] #res
		#------------------------ "b" done --------------------------
		c = "c"
		backtrack("c")
			#doesn't hit base case
			for c in "def"
				c="d"
				backtrack("cd")
					#hits base case
					["ad","ae","af","bd","be","bf","cd"] #res
					return 
				c="e"
				backtrack("ce")
					#hits base case
					["ad","ae","af","bd","be","bf","cd","ce"] #res
					return
				c="f"
				backtrack("cf")
					#hits base case
					["ad","ae","af","bd","be","bf","cd","ce","cf"]  #res
					return
				#for loop ends
			return ["ad","ae","af","bd","be","bf","cd","ce","cf"]  #res
		#------------------------ "c" done --------------------------
		
	return ["ad","ae","af","bd","be","bf","cd","ce","cf"] #res
```

#### “A journey of a thousand miles must begin with a single step.” — Lao Tzu.


