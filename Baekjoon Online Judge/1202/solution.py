'''
보석과 가방을 모두 가벼운 순서로 정렬하고
우선순위 큐에 가장 가벼운 가방 무게 이하의 보석들을 넣고 
그 중 가장 높은 가격의 보석으로 가방을 소모시켜나간다.

또는 

보석들을 비싼 순서, 가벼운 순서로 정렬하고,
앞에서부터 보석을 확인해가면서 해당 무게를 담을 수 있는 최소 크기의 가방을 소모시킨다.
이분탐색 및 링크드리스트를 활용해서 매번 최소 크기의 가방을 효율적으로 찾고 소모시킨다.
링크드리스트의 임의의 노드를 O(1)에 접근하기 위해 모든 노드를 가방의 크기를 키로 하는 딕셔너리에 저장한다.
'''
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

gems = [ 
    tuple(map(int, input().split()))
    for _ in range(N)
]
gems.sort(reverse=True) # stack으로 사용

bag_capacities = [ int(input()) for _ in range(K) ]
bag_capacities.sort()

lighter_gems = [] # 가장 가벼운 가방 무게 이하의 보석의 가격에 대한 최대 우선순위 큐

total_price = 0

for capacity in bag_capacities:
    # 현재 가장 가벼운 가방의 무게 이하의 보석을 우선순위 큐로 옮긴다.
    while gems and gems[-1][0] <= capacity:
        _, price = gems.pop()
        heapq.heappush(lighter_gems, -price)

    # 현재 가장 가벼운 가방의 무게 이하의 보석이 있는 경우,그 중 가장 높은 가격의 보석을 담는다.
    if lighter_gems:
        price = -heapq.heappop(lighter_gems)
        total_price += price

print(total_price)