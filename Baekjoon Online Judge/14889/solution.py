import sys
from itertools import combinations, permutations

input = sys.stdin.readline

N = int(input())
S = [ list(map(int, input().split())) for _ in range(N) ]

min_diff = float('inf')

# 시간복잡도는 O(NC0.5N * 0.5NP2)인데, N이 최대 20이므로, 완전탐색이 가능하다.
for team in combinations(range(N), N // 2):
    other_team = [p for p in range(N) if p not in team]

    team_ability = sum([S[i][j] for i, j in permutations(team, 2)])
    other_team_ability = sum([S[i][j] for i, j in permutations(other_team, 2)])

    min_diff = min(min_diff, abs(team_ability - other_team_ability))

print(min_diff)
