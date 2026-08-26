class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i = j = count = 0
        min_len = float('inf')
        ans = ""

        while j < len(s):
            if s[j] == "1":
                count += 1

            while count == k:
                curr_subs = s[i:j + 1]

                if len(curr_subs) < min_len or (len(curr_subs) == min_len and curr_subs < ans):
                    ans = curr_subs
                    min_len = len(curr_subs)

                if s[i] == "1":
                    count -= 1
                i += 1

            j += 1
        return ans