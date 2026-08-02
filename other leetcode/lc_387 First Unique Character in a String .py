class Solution:
    def firstUniqChar(self, s: str) -> int:
        charList = list(s)
        cnt = Counter(charList)

        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i

        return -1