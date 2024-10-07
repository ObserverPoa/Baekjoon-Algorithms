'''
센서들의 좌표를 중복 없이 만들고 오름차순으로 정렬해서, 인접 센서간의 거리를 전부 구한다.
그 다음, 가장 큰 센서간 거리를 한개씩 지워가며 집중국의 개수를 한개 늘린다. 
그렇게 집중국의 개수가 K개가 될때까지 반복한다.
'''
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

sensors = list(set(map(int, input().split())))
sensors.sort()

gaps = [] # 인접 센서간의 거리

for i in range(1, len(sensors)):
    gaps.append(sensors[i] - sensors[i - 1])

gaps.sort(reverse=True)

# 모든 센서를 수신하는 한개의 집중국의 수신 길이에서, K-1개의 가장 큰 인접 센서간 거리를 뺸다.
print(sensors[-1] - sensors[0] - sum(gaps[:K - 1]))