class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)

        for char in ransomNote:
            if cnt[char] > 0:
                cnt[char] -= 1
            else: return False
        return True

