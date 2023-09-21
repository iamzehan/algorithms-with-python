import pprint
def count_letters(string):
	ans={}
	for i in string:
		if i==" ":
			continue
		else:
			if i not in ans.keys():
				ans[i]=1
			else:
				ans[i]+=1
	return ans
if __name__ == "__main__":
	string = "happy birthday to you"
	pprint.pprint(count_letters(string))
