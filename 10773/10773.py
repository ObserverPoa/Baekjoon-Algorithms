import sys

input_count = int(sys.stdin.readline().split()[0])

numbers = []
for i in range(input_count):
    input = int(sys.stdin.readline().split()[0])
    if input == 0 and len(numbers):
        numbers.pop()
    else:
        numbers.append(input)

sum = 0
for number in numbers:
    sum += number

print(sum)
