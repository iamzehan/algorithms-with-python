n = 5
pos1, pos2 = [4, 3]
obs = [[2, 3], [4, 2], [5, 5]]

down = [[pos1-i,pos2] for i in range(1,pos1)]
print(down)

up = [[pos1+i,pos2] for i in range(1,n-pos1+1)]
print(up)

left = [[pos1, pos2-i] for i in range(1,n-pos2+1)]
print(left)
right = [[pos1, pos2+i] for i in range(1,n-pos2+1)]
print(right)

right_up = [[pos1+i, pos2+i] for i in range(1,n-max(pos1,pos2)+1)]
print(right_up)
left_up = [[pos1+i, pos2-i] for i in range(1,n-max(pos1,pos2)+1)]
print(left_up)

