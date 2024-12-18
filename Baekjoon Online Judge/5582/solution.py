import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

max_len = 0

for offset in range(len(str1)):
    str1_sub = str1[offset:]
    restart_points = [0]

    # 재시작 지점 생성
    for i in range(1, len(str1_sub)):
        if str1_sub[restart_points[-1]] == str1_sub[i]:
            restart_points.append(restart_points[-1] + 1)
        else:
            restart_points.append(0)

    str1_sub_idx = 0

    for char in str2:
        if char == str1_sub[str1_sub_idx]:
            str1_sub_idx += 1
        else:
            # 재시작 지점을 일치할떄까지 거슬러올라간다.
            while str1_sub_idx > 0:
                str1_sub_idx = restart_points[str1_sub_idx - 1]
                if char == str1_sub[str1_sub_idx]:
                    str1_sub_idx += 1
                    break

        max_len = max(max_len, str1_sub_idx)

        if str1_sub_idx == len(str1_sub):
            break
    
    if max_len == min(len(str1), len(str2)):
        break

print(max_len)