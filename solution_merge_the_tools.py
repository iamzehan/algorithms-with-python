def merge_the_tools(string, k):
    splits = [(string[i:i+k]) for i in range(0, len(string), k)]
    def find_unique(s):
        new_s=''
        for i in range(len(s)):
            if i==0:
                new_s+=s[i]
            elif s[i] not in new_s:
                new_s+=s[i]
        return new_s

    for result in [ find_unique(i) for i in splits]:
        print(result)
