N = int(input())
characters = list(input().strip())

min_required_count = max(
    0,
    6 - len(characters),
    sum([
        all(map(lambda x: x == x.upper(), characters)),
        all(map(lambda x: x == x.lower(), characters)),
        all(map(lambda x: not x.isnumeric(), characters)),
        all(map(lambda x: x not in '!@#$%^&*()-+', characters)),
    ])
)

print(min_required_count)


