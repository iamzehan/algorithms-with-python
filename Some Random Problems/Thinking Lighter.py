n = 5
pos1, pos2 = [4, 3]
obs = [[2, 3], [4, 2], [5, 5]]
moves={}
moves["down"] = [[pos1-i,pos2] for i in range(1,pos1)]
moves["up"]= [[pos1+i,pos2] for i in range(1,n-pos1+1)]
moves["left"] = [[pos1, pos2-i] for i in range(1,pos2)]
moves["right"] = [[pos1, pos2+i] for i in range(1,n-pos2+1)]
moves["right_up"] = [[pos1+i, pos2+i] for i in range(1,n-max(pos1,pos2)+1)]
moves["left_up"]= [[pos1+i, pos2-i] for i in range(1,n-max(pos1,pos2)+1)]
moves["right_down"] = [[pos1-i, pos2+i] for i in range(1,n-min(pos1,pos2)+1)]
moves["left_down"] = [[pos1-i, pos2-i] for i in range(1,n-min(pos1,pos2)+1)]
print(moves)
total=0
for move in moves.values():
    for m in move:
        if m in obs:
            break
        total+=1
print(total)
