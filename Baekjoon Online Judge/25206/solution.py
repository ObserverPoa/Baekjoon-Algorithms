'''
dict에 등급에 따른 과목평점을 저장해서 계산에 사용한다.
'''
import sys

input = sys.stdin.readline

score_by_grade = {
    'A+': 4.5,
    'A0': 4,
    'B+': 3.5,
    'B0': 3,
    'C+': 2.5,
    'C0': 2,
    'D+': 1.5,
    'D0': 1,
    'F': 0,
}

total_credit = 0
score_sum = 0

for _ in range(20):
    args = input().strip().split()
    credit = int(args[1].split('.')[0])
    grade = args[2]
    if grade == 'P': 
        continue

    score_sum += credit * score_by_grade[grade]
    total_credit += credit

print(score_sum / total_credit)

