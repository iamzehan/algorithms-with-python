import pprint

pages= {"A": "Hi there",
        "B": "Hi Adit",
        "C": "There we go",
        "D": "There there",
        "E": "Go go go"
        }
        
ans = {}

for page in pages.keys():
    location=1
    for word in pages[page].title().split(' '):
        if word not in ans.keys():
            ans[word]=[[page,location]]
        else:
            ans[word].append([page,location])
        location+=1
        
pprint.pprint(ans)
print("\nAnother way to store the data\n")

ans= {}
for page in pages.keys():
    location=1
    for word in pages[page].title().split(' '):
        if word not in ans.keys():
            ans[word]={page:[location]}
        else:
            if page in ans[word].keys():
                ans[word][page].append(location)
            else:
                ans[word][page]=[location]
        location+=1
pprint.pprint(ans)

print("\nBecause dictionaries would only store the last found value of the key \nand store it against the key, so we are going to have to use list to\ncompensate for that")
