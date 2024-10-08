import sys

input = sys.stdin.readline

document = input().strip()
keyword = input().strip()

idx = 0
count = 0
while idx < len(document):
    if keyword == document[idx:idx + len(keyword)]:
        count += 1
        idx += len(keyword)
    else:
        idx += 1

print(count)