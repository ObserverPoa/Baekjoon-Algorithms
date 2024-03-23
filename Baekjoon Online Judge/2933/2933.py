import sys
import collections

R, C = map(int, sys.stdin.readline().split())

cave = [
    [slot for slot in sys.stdin.readline().strip()]
    for _ in range(R)
]

N = int(sys.stdin.readline())

stick_heights = list(map(int, sys.stdin.readline().split()))

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs(x, y, visited, group):
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    group.append((x, y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < R and \
                0 <= y + dy < C and \
                (x + dx, y + dy) not in visited and \
                cave[x + dx][y + dy] == 'x':
                visited.add((x + dx, y + dy))
                group.append((x + dx, y + dy))
                queue.append((x + dx, y + dy))


def find_floating_group():
    visited = set()

    for x in range(R):
        for y in range(C):
            if cave[x][y] == 'x' and (x, y) not in visited:
                group = []
                bfs(x, y, visited, group)
                
                if not any(i == R - 1 for i, _ in group):
                    return group

def drop_floating_group():
    group = find_floating_group()
    if group is None:
        return
    
    max_x_by_y = [-1 for _ in range(C)]

    for x, y in group:
        max_x_by_y[y] = max(x, max_x_by_y[y])


    min_distance = R

    for y, man_x in enumerate(max_x_by_y):
        if man_x == -1:
            continue

        distance = 0
        for i in range(man_x + 1, R):
            if cave[i][y] == 'x':
                break
            distance += 1
        
        min_distance = min(min_distance, distance)
    
    for x, y in group:
        cave[x][y] = '.'

    for x, y in group:
        cave[x + min_distance][y] = 'x'



from_left = True

for stick_height in stick_heights:
    stick_x = R - stick_height

    indices = range(C) if from_left else range(C - 1, -1, -1)

    for i in indices:
        if cave[stick_x][i] == 'x':
            cave[stick_x][i] = '.'
            drop_floating_group()
            break

    from_left = not from_left

for row in cave:
    print(''.join(row))
