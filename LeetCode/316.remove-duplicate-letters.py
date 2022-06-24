#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        # 각 문자의 마지막 등장 인덱스 정리.
        last_index = {
            s[i]: i for i in range(len(s))
        }

        # 스택에 문자가 있는지 여부를 빠르게 조회하기 위함
        exist = collections.defaultdict(bool)

        # 스택에 차례로 넣으면서, 사전순서가 아닌데 뒤에 더 있는 것에 대해서는 팝핑한뒤 넣음
        uniques = []
        for i in range(len(s)):
            if exist[s[i]]:
                continue # 동일한 문자가 이미 스택에 들어있다면, 그것보다 더 나은 위치는 존재할 수 없기 때문에 건너뛰어도 되는 것이다.

            while uniques and uniques[-1] > s[i] and last_index[uniques[-1]] > i:
                exist[uniques.pop()] = False
            
            uniques.append(s[i])
            exist[s[i]] = True
        
        return ''.join(uniques)


        # 책의 recursive 풀이 해석: 
        # 남은 배치해야할 모든 문자를 뒤에 오게 할 수 있는 문자 중에서 사전적으로 가장 낮은 걸 반복적으로 선택해 간다.

            

# @lc code=end

