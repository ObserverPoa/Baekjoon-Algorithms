'''
서류 순위가 더 높은 사람들보다 면접 순위가 더 높아야 한다.
서류 순위가 더 높은 사람들의 최고 면접 순위보다 더 높은 사람을 카운팅한다.
'''
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    ranks = [
        tuple(map(int, input().split())) for _ in range(N)
    ]

    best_interview_rank = N + 1
    count = 0

    # 서류 순위가 높은 사람부터 확인해서 서류 순위가 더 높은 사람들의 최고 면접 순위를 갱신한다.
    for _, interview_rank in sorted(ranks):
        if interview_rank < best_interview_rank:
            count += 1
            best_interview_rank = interview_rank

    print(count)