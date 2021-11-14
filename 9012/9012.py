import sys

input_count = int(sys.stdin.readline())
ps_list = [sys.stdin.readline().rstrip() for i in range(input_count)]

for ps in ps_list:
    level = 0
    for char in ps:
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1

        if level < 0:
            break
        
    if level == 0:
        print("YES")
    else:
        print("NO")
