class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word[0] == ch:
            return word
        temp = word[0]
        for i in range(1, len(word) - 1):
            if word[i] == ch:
                temp += word[i]
                return temp[::-1] + word[i + 1:]
            temp += word[i]
        if word[-1] == ch:
            return word[::-1]
        return word
