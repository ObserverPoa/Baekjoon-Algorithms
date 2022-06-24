#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start



class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import collections
        
        words = []
        chars = []

        def flush_chars():
            word = ''.join(chars).lower()
            if word not in banned:
                words.append(word)
            chars.clear()

        for char in paragraph:
            if char.isalpha():
                chars.append(char)
            elif chars:
                flush_chars()
        if chars:
            flush_chars()


        return collections.Counter(words).most_common(1)[0][0]

        

        


# @lc code=end

