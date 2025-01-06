import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())
r, c = r - 1, c - 1

array = [ list(map(int, input().split())) for _ in range(3) ]

def do_R_operation():
    for i, row in enumerate(array):
        counter = Counter(row)
        del counter[0]
        
        new_row = []
        for value, count in sorted(counter.items(), key=lambda item: (item[1], item[0])):
            new_row.append(value)
            new_row.append(count)
            
        array[i] = new_row
    
    max_len = max(map(len, array))
    for i in range(len(array)):
        array[i].extend([0] * (max_len - len(array[i])))

def do_C_operation():
    width = len(array[0])
    for i in range(width):
        column = [array[x][i] for x in range(len(array))]
        counter = Counter(column)
        del counter[0]

        new_col = []
        for value, count in sorted(counter.items(), key=lambda item: (item[1], item[0])):
            new_col.append(value)
            new_col.append(count)
        
        # 새로운 열의 길이가 더 길 경우, 0으로된 행들을 끝에 추가
        if len(array) < len(new_col):
            array.extend([[0] * width for _ in range(len(new_col) - len(array))])
        
        # 새로운 열로 덮어씌운다.
        for x in range(len(new_col)):
            array[x][i] = new_col[x]
        
        # 새로운 열로 덮어씌우고 남은 뒷부분은 0으로 채운다.
        for x in range(len(new_col), len(array)):
            array[x][i] = 0
    
    # 0으로만 이루어진 행들을 끝에서 제거
    while not any(array[-1]):
        array.pop()


def get_min_time():
    for time in range(101):
        if len(array) > r and len(array[r]) > c and array[r][c] == k:
            return time
    
        if len(array) >= len(array[0]):
            do_R_operation()
        else:
            do_C_operation()

    return -1

print(get_min_time())