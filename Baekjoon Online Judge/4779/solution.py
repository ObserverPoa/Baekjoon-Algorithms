'''
재귀적으로 n을 3등분해서, 가운데는 공백문자를 두고, 
양쪽은 길이가 1이 되었을때 -를 둔다.
'''
import sys

input = sys.stdin.readline

def cantor(n):
    if n == 1:
        return '-'
    
    next_n = n // 3
    line_part = cantor(next_n) 
    return line_part + (' ' * next_n) + line_part


while True:
    line = input()
    if not line:
        break

    n = int(line)
    print(cantor(3 ** n))

