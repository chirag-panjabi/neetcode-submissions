class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        mx = 0
        for i in range(len(s)):
            c = s[i]
            freq[c] = freq.get(c,0) + 1
            # while len(freq) > 2:
            #     freq[s[left]] -= 1
            #     if freq[s[left]] == 0:
            #         del freq[s[left]]
            #     left += 1
            
            while len(freq) >= 2 and ((i-left+1) - max(freq.values())) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            mx = max(mx, i - left + 1)
        
        return mx
