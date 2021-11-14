import sys

step = [[0, -1], [1, 0], [0, 1], [-1, 0]]
next_direction = [3, 2, 1, 0]

room_depth, room_width = list(map(int, sys.stdin.readline().split()))
row, col, direction = list(map(int, sys.stdin.readline().split()))
room = [list(map(int, sys.stdin.readline().split())) for i in range(room_depth)]

counter = 0
while True:
    if room[row][col] == 0:
        room[row][col] = 2
        counter += 1
    
    if room[row + step[0 - direction][0]][col + step[0 - direction][1]] == 0:
        row += step[0 - direction][0]
        col += step[0 - direction][1]
        direction = next_direction[0 - direction]
    elif room[row + step[1 - direction][0]][col + step[1 - direction][1]] == 0:
        row += step[1 - direction][0]
        col += step[1 - direction][1]
        direction = next_direction[1 - direction]
    elif room[row + step[2 - direction][0]][col + step[2 - direction][1]] == 0:
        row += step[2 - direction][0]
        col += step[2 - direction][1]
        direction = next_direction[2 - direction]
    elif room[row + step[3 - direction][0]][col + step[3 - direction][1]] == 0:
        row += step[3 - direction][0]
        col += step[3 - direction][1]
        direction = next_direction[3 - direction]
    elif room[row + step[1 - direction][0]][col + step[1 - direction][1]] == 2:
        row += step[1 - direction][0]
        col += step[1 - direction][1]
    else:
        break
print(counter)
    