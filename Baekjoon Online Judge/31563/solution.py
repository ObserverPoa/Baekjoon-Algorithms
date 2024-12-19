import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
sequence = list(map(int, input().split()))

cumulative_sums = [sequence[0]]
for i in range(1, N):
    cumulative_sums.append(cumulative_sums[-1] + sequence[i])

offset = 0
for _ in range(Q):
    args = input().strip().split()
    if args[0] == '1':
        offset -= int(args[1])
        if offset < 0:
            offset += N
    elif args[0] == '2':
        offset = (offset + int(args[1])) % N
    elif args[0] == '3':
        a, b = int(args[1]) - 1, int(args[2]) - 1
        left = (a + offset) % N
        right = (b + offset) % N

        range_sum = 0
        if left <= right:
            range_sum += cumulative_sums[right]
            if left > 0:
                range_sum -= cumulative_sums[left - 1]
        else:
            range_sum += cumulative_sums[right]
            range_sum += cumulative_sums[-1] - cumulative_sums[left - 1]
        
        print(range_sum)
        


