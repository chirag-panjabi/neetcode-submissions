from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # freq = set()
        # mx = 0
        # l = 0
        # for r in range(len(s)):
        #     if s[r] not in freq:
        #         freq.add(s[r])
        #     while s[r] in freq:
        #         freq.remove(s[l])
        #         l += 1  
        #     mx = max(mx, len(freq))
        # return mx

        freq = defaultdict(int)
        mx= 0
        r = 0
        l = 0
        n = len(s)
        while r < n:
            freq[s[r]] += 1
            while l<r and freq.get(s[r]) > 1:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            mx = max(mx, r-l+1)
            r += 1

        return mx



