def down(pos,obs):
    down=0
    while pos[0]>1:
        pos[0] -= 1
        if pos in obs:
            break
        else:
            down+=1
    return down

def up(pos,obs,n=8):
    up=0
    while pos[0]<n:
        pos[0] += 1
        if pos in obs:
            break
        else:
            up+=1
    return up

def left(pos,obs):
    left=0
    while pos[1]>1:
        pos[1] -= 1
        if pos in obs:
            break
        else:
            left+=1
    return left

def right(pos,obs,n=8):
    right=0
    while pos[1]<n:
        pos[1] += 1
        if pos in obs:
            break
        else:
            right+=1
    return right

def right_up(pos,obs,n=8):
    right_up=0
    while pos[0]<n:
        pos[0],pos[1]=pos[0]+1,pos[1]+1
        if pos in obs:
            break
        else:
            right_up+=1
    return right_up
    
def right_down(pos,obs,n=8):
    right_down=0
    while pos[0]>1 and pos[1]<n:
        pos[0],pos[1]=pos[0]-1,pos[1]+1
        if pos in obs:
            break
        else:
            right_down+=1
    return right_down
    
def left_up(pos,obs,n=8):
    left_up=0
    while pos[0]<n and pos[1]>1:
        pos[0],pos[1]=pos[0]+1,pos[1]-1
        if pos in obs:
            break
        else:
            left_up+=1
    return left_up
    
def left_down(pos,obs):
    left_down=0
    while pos[0]>1 and pos[1]>1:
        pos[0],pos[1]=pos[0]-1,pos[1]-1
        if pos in obs:
            break
        else:
            left_down+=1
    return left_down

print("down: ", down([4,4],[[3,5]]))
print("up: ", up([4,4],[[3,5]]))
print("left: ",left([4,4],[[3,5]]))
print("right: ",right([4,4],[[3,5]]))
print("right_up: ", right_up([4,4],[[3,5]]))
print("right_down: ", right_down([4,4],[[3,5]]))
print("left_up: ", left_up([4,4],[[3,5]]))
print("left_down: ", left_down([4,4],[[3,5]]))

#link: https://www.hackerrank.com/challenges/queens-attack-2/problem
