from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return Counter(s) == Counter(t)
        # this is not good approch for interview
        # unless you explain the underlying principle of COunter

        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')] += 1
            freq[ord(t[i])-ord('a')] -= 1
        
        return all(c==0 for c in freq)
        
    # this way of looping in notes, i did not know this        
    # for a, b in zip(s, t):
    #     count[ord(a) - ord('a')] += 1   # increment for s
    #     count[ord(b) - ord('a')] -= 1   # decrement for t
