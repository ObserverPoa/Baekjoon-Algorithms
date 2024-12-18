'''
남은 개수가 2개일때 자신의 턴이면 무조건 패배한다.
라는 사실로부터 역추적 해나가면
자신의 턴일때 무조건 패배하는 남은 갯수의 패턴이 보인다.
그것은 7로 나눴을때 나머지가 0 또는 2인 지점이다. 
'''
import sys

input = sys.stdin.readline

N = int(input())

if N % 7 == 0 or N % 7 == 2:
    print('CY')
else:
    print('SK')
