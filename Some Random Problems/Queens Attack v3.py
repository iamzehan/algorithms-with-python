#!/bin/python3
import os

def queensAttack(n, k, r_q, c_q, obs):

    obs_set = set((r, c) for r, c in obs)
    
    moves = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Right Down
        (-1, 1),  # Right Up
        (1, -1),  # Left Down
        (-1, -1), # Left Up
    ]
    
    max_moves = 0

    for move in moves:
        dx, dy = move
        pos1, pos2 = r_q + dx, c_q + dy
        moves_in_direction = 0
        
        while 1 <= pos1 <= n and 1 <= pos2 <= n and (pos1, pos2) not in obs_set:
            moves_in_direction += 1
            pos1 += dx
            pos2 += dy
        
        max_moves += moves_in_direction
    
    return max_moves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
