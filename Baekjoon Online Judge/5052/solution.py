'''
전화번호는 서로 다름이 보장된다.
어떤 전화번호가 다른 전화번호의 접두사인지 확인하면 된다.
모든 전화번호로 만들 수 있는 접두사들을 set에 저장한다. 
단, 완전한 전화번호는 제외하고 저장해야 한다.
일치했을때 자신의 전화번호와 일치한건지 다른 전화번호의 접두사와 일치한건지 알 수가 없기 때문.
'''
import sys

input = sys.stdin.readline

test_case_count = int(input())

def are_consistent(tel_numbers):
    prefixes = set()

    # 모든 전화번호의 접두사 저장
    for tel_number in tel_numbers:
        for i in range(1, len(tel_number)):
            prefixes.add(tel_number[:i])
    
    # 접두사와 일치하는 전화번호가 있는지 확인
    for tel_number in tel_numbers:
        if tel_number in prefixes:
            return False
    return True

for _ in range(test_case_count):
    n = int(input())

    tel_numbers = [input().strip() for _ in range(n)]

    if are_consistent(tel_numbers):
        print("YES")
    else:
        print("NO")
