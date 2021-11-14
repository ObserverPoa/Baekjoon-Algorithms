import sys

numCnt = int(sys.stdin.readline())
numStr = sys.stdin.readline()

sum = 0
for i in range(numCnt):
    sum += int(numStr[i])
print(sum)