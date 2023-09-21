def is_palindrome(string):
    i = 0
    j = len(string)-1
    while i<j:
        if string[i]==string[j]:
            i+=1
            j-=1
        else:
            return False
    
    return True
if __name__ == "__main__":
    for string in "civic,radar,level,rotor,kayak,madam,refer".split(","):
        print(string,":",is_palindrome(string))
