def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        split=string[i:i+k]
        new=''
        for j in split:
            if j == 0:
                new+=j 
            else:
                if j not in new:
                    new+=j
        print(new) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
