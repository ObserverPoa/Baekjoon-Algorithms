'''
3의 배수는 모든 자리의 숫자를 더해서 3으로 나누어떨어져야 한다는 사실을 이용한다.
추가적으로, 30으로 나누어 떨어지는 수는 1의자리가 0이여야 한다. 
'''
import sys

input = sys.stdin.readline

numbers = [int(char) for char in input().strip()]
numbers.sort(reverse=True)

if sum(numbers) % 3 != 0 or numbers[-1] != 0:
    print(-1)
else:
    for number in numbers:
        print(number, end="")
    print()
