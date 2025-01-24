formula = input().strip()

priorities = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

stack = []
output = []

for char in formula:
    if char.isalpha():
        output.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack[-1] != '(':
            output.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] in priorities and priorities[char] <= priorities[stack[-1]]:
            output.append(stack.pop())
        stack.append(char)

while stack:
    output.append(stack.pop())

print(''.join(output))
            
            