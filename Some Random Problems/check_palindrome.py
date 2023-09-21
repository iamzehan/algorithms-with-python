def is_palindrome(string):
    i = 0
    j = len(string)-1
    while i>j:
        if string[i]==string[j]:
            i+=1
            j-=1
        else:
            return False
    
    return True
string = "racecar"
print(is_palindrome(string))
