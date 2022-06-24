#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        # trie 구축
        root = {}
        for i in range(len(words)):
            node = root
            for char in words[i]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[None] = i

        result = []

        def is_palindrome(word):
            return word == word[::-1]

        def dfs(node, path, i):
            for char in node:
                if char is None and path and is_palindrome(path):
                    result.append([node[None], i])
                elif char is not None:
                    path.append(char)
                    dfs(node[char], path, i)
                    path.pop()
        
        # Trie에 있는 단어를 앞에, word를 뒤에 둬서 합쳤을 때의 palindrome 체크
        def check_palindrome(i, word):
            node = root

            # trie에서 word길이보다 짧은 단어를 매치해서 word의 남은 부분이 palindrome이면 result에 추가.
            for j, char in enumerate(word[::-1]):
                if None in node and is_palindrome(word[::-1][j:]):
                    result.append([node[None], i])

                if char in node:
                    node = node[char]
                else:
                    return

            # word와 똑같은 길이로 매치되고(word를 뒤집은게 trie에 있을 경우), 자신이 아닌 경우 result에 추가
            if None in node and node[None] != i:
                result.append([node[None], i])
            
            # trie에서 word를 전부 매치 후, trie의 남은 부분(node의 서브트리)를 dfs로 탐색해서 palindrome인 것들에 대해 result에 추가.
            dfs(node, [], i)
        
        for i, word in enumerate(words):
            check_palindrome(i, word)

        return result

# @lc code=end

