def down(pos1,pos2,obs):
    down=0
    pos=[pos1,pos2]
    while pos[0]>1:
        pos[0] -= 1
        if pos in obs:
            break
        else:
            down+=1
    return down

def up(pos1,pos2,obs,n):
    up=0
    pos=[pos1,pos2]
    while pos[0]<n:
        pos[0] += 1
        if pos in obs:
            pos=[]
            break
        else:
            up+=1
    return up

def left(pos1,pos2,obs):
    left=0
    pos=[pos1,pos2]
    
    while pos[1]>1:
        pos[1] -= 1
        if pos in obs:
            break
        else:
            left+=1
    return left

def right(pos1,pos2,obs,n):
    right=0
    pos=[pos1,pos2]
    while pos[1]<n:
        pos[1] += 1
        if pos in obs:
            break
        else:
            right+=1
    return right

def right_up(pos1,pos2,obs,n):
    right_up=0
    pos=[pos1,pos2]
    while pos[0]<n:
        pos[0],pos[1]=[pos1,pos2][0]+1,pos[1]+1
        if pos in obs:
            break
        else:
            right_up+=1
    return right_up
    
def right_down(pos1,pos2,obs,n):
    right_down=0
    pos=[pos1,pos2]
    while pos[0]>1 and pos[1]<n:
        pos[0],pos[1]=[pos1,pos2][0]-1,pos[1]+1
        if pos in obs:
            break
        else:
            right_down+=1
    return right_down
    
def left_up(pos1,pos2,obs,n):
    left_up=0
    pos=[pos1,pos2]
    while pos[0]<n and pos[1]>1:
        pos[0],pos[1]=[pos1,pos2][0]+1,pos[1]-1
        print(pos1,pos2)
        if pos in obs:
            break
        else:
            left_up+=1
    return left_up
    
def left_down(pos1,pos2,obs):
    left_down=0
    pos=[pos1,pos2]
    while pos[0]>1 and pos[1]>1:
        pos[0],pos[1]=[pos1,pos2][0]-1,pos[1]-1
        if pos in obs:
            break
        else:
            left_down+=1
    return left_down


n=5
pos1,pos2=[4,3]
obs = [[2,3],[4,2],[5,5]]
print(left(pos1,pos2,obs))
print(right(pos1,pos2,obs,n))
