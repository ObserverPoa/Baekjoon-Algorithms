''' 
팰린드롬은 좌우 대칭인 문자열이다.
팰린드롬이 아닐 때, 문자 한 개를 제거하면 팰린드롬이 되는지 판별해야 한다.
투포인터를 사용해서 좌우를 짝지어가며 범위를 좁혀가다가 처음으로 짝을 지을 수 없는 경우,
둘 중 한개를 제거했을때 두 경우 중 한가지 경우 이상 팰린드롬이 되는지 확인한다.
'''
import sys

input = sys.stdin.readline

def is_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def determine_palindrome_type(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
            continue

        if is_palindrome(string, left + 1, right) or is_palindrome(string, left, right - 1):
            return 1
        else:
            return 2
        
    return 0


T = int(input())

for _ in range(T):
    print(determine_palindrome_type(input().strip()))



