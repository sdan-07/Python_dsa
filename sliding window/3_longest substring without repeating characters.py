class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        i=0
        j=0
        max_len = 0

        while j<len(s):
            while s[j] in charset:
                charset.remove(s[i])
                i+=1

            charset.add(s[j])
            max_len = max(max_len, j-i+1)
            j+=1

        return max_len