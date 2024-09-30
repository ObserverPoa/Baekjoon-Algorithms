'''
이동 거리를 최소화 하기 위해, 거리가 먼 곳을 먼저 방문한다.
원점에 오면 책의 개수가 완전히 채워지므로, 왼쪽과 오른쪽을 독립적으로 계산 가능하다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

books = list(map(int, input().split()))

left_books = [] # 음수 책 좌표
right_books = [] # 양수 책 좌표

for book in books:
    if book > 0:
        right_books.append(book)
    else:
        left_books.append(-book)

left_books.sort() # 스택으로 사용
right_books.sort() # 스택으로 사용

# 가장 먼곳을 방문하고 책을 놓은 개수 만큼 pop하는것을 반복
def count_steps(books: list[int]):
    count = 0
    while books:
        count += books[-1] * 2
        for _ in range(min(M, len(books))):
            books.pop()
    return count

total_count = 0

# 마지막에는 원점으로 돌아가지 않아도 되므로, 통합적으로 가장 먼 좌표만 별도로 처리
if left_books and (not right_books or left_books[-1] > right_books[-1]):
    total_count += left_books[-1]
    for _ in range(min(M, len(left_books))):
        left_books.pop()
elif right_books and (not left_books or right_books[-1] > left_books[-1]):
    total_count += right_books[-1]
    for _ in range(min(M, len(right_books))):
        right_books.pop()

total_count += count_steps(left_books)
total_count += count_steps(right_books)

print(total_count)