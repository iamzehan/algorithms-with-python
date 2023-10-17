def splitString(s):
    def dfs(idx, prev):
        if len(s)==idx:
            return True
        for i in range(idx,len(s)):
            val = int(s[idx:i+1])
            print(f"Value: {val}, Previous:{prev}")
            if val==prev-1 and dfs(i+1, val):
                return True
        return False 

    for i in range(len(s)-1):
        val = int(s[:i+1])
        print("Current: ", val)
        if dfs(i+1, val):
            return True
    return False

print(splitString("0090089"))

"""
Explanation:

def splitString("0090089"):
	for i in range(7-1):
		#iteration 1
		i = 0
		val = int(s[:0+1]) = int("0") = 0
		if dfs(idx=1,prev=0):
			#ignore
			for i in range(1,7):
				i = 1
				val = int(s[1 : 2]) = int("0") = 0
				if 0 == 0-1 #stop
				i = 2
				val = int(s[1 : 3]) = int("09") = 9
				if 9 == 0-1 #stop
				i = 3
				val = int(s[1 : 4]) = int("090") = 90
				if 90 == 0-1 #stop
				i = 5
				val = int(s[1 : 5]) = int("0900") = 900
				if 900 == 0-1 #stop
				i = 6
				val = int(s[1 : 6]) = int("09008") = 9008
				if 9008 == 0-1 #stop
			return False
		
		# iteration 2
		i = 1
		val = int(s[:1+1]) = int("00") = 0
		if dfs(idx=2, prev = 0):
			#ignore
			for i in (2,7):
				i = 2
				val = int(s[2 : 3]) = int("9") = 9
				if 9 == 0-1 #stop
				i = 3
				val = int(s[2 : 4]) = int("90") = 90
				if 90 == 0-1 #stop
				i = 4
				val = int(s[2 : 5]) = int ("900") = 900
				if 900 == 0-1 #stop
				i = 5
				val = int(s[2 : 6]) = int ("9008") = 9008
				if 9008 == 0-1 #stop
				i = 6
				val = int(s[2 : 7]) = int ("90089") = 90089
				if 90089 == 0-1 #stop
			return False 
		
		#iteration 3
		i = 2
		val = int(s[:2+1]) = int(s[:3] = int("009") = 9
		if dfs(idx =3, prev = 9):
			#ignore
			for i in (3,7):
				i = 3
				val = int(s[3 : 4]) = int("0") = 0
				if 0 == 9-1 #stop
				i = 4
				val = int(s[3 : 5]) = int("00") = 0
				if 0 == 9-1 #stop
				i = 5
				val = int(s[3 : 6]) = int("008") = 8
				if 8 == 9-1 and dfs(idx = 5+1 = 6, prev = 8):
									#ignore
									for i in (6,7):
										i = 6
										val = int([6: 7]) = int("9") = 9
										if 9 == 8 - 1 # stop
									return False 
				i = 6 
				val = int(s[3 : 7]) = int("0089")= 89
				if 89 == 9-1 #stop
			return False 
		i = 3 
		val = int(s[:3+1]) = int(s[:4] = int("0090") = 90
		if dfs(idx =4, prev = 90):
			#ignore
			for i in range(4,7):
				i = 4
				val = int(s[4 : 5]) = int("0") = 0
				if 0 == 90 -1 # stop
				i = 5
				val = int(s[4 : 6]) = int("08") = 8
				if 8 == 90 -1 # stop
				i = 6
				val = int(s[4 : 7]) = int("089") = 89
				if 89 == 90 -1 and dfs(idx = 6+1 = 7, prev = 89):
									if idx == len(s): # yes
										return True
					return True
			return True

"""
