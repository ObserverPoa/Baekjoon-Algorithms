'''
- 연산자 뒤의 모든 수는 괄호를 통해 음수로 만들 수 있다.
왼쪽부터 문자를 판단해서 -가 나오기 전까지는 양수를 결과에 더하고, 나온 후에는 음수를 결과에 더한다.
'''
import sys

input = sys.stdin.readline

result = 0
number = ''
positive = True

for char in input().strip():
    if char.isnumeric():
        number += char
    else:
        result += int(number) if positive else -int(number)
        number = ''
    
    if char == '-':
        positive = False

result += int(number) if positive else -int(number)

print(result)