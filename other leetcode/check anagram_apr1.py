class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        return cnt_t == cnt_s

        # if len(s) != len(t): return False
        # i=j=0
        # count=0

        # while i<len(s):
        #     if s[i] in t:
        #         count+=1

        # if count == len(s):
        #     return True
        # return False