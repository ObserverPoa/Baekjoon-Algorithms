'''
최대 학생수는 1000명으로, O(n^2)으로 학생마다 전체 테이블을 제한시간 내에 순회할 수 있다.
'''
import sys

input = sys.stdin.readline

N = int(input())

class_lists = [ list(map(int, input().split())) for _ in range(N) ]

temp_leader_num = None # 임시 반장 번호
max_known_count = -1 # 같은 반이였던 학생 수의 최대값

for student_num, class_list in enumerate(class_lists):
    known_students = set()
    for j, class_num in enumerate(class_list):
        for i in range(N):
            if i != student_num and class_lists[i][j] == class_num: 
                known_students.add(i)
    
    if temp_leader_num is None or len(known_students) > max_known_count:
        temp_leader_num = student_num
        max_known_count = len(known_students)

print(temp_leader_num + 1)


