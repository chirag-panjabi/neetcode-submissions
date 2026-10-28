class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        c1 = Counter(s1)
        l = len(s1)
        c2 = {}
        
        # creating window of size L
        for i in range(l):
            ch = s2[i]
            c2[ch] = c2.get(ch, 0) + 1
        
        p = 0
        if c1 == c2:
            return True
        
        
        for i in range(l, len(s2)):
            char = s2[i]
            c2[char] = c2.get(char, 0) + 1
            c2[s2[p]] -= 1
            if c2[s2[p]] == 0:
                del c2[s2[p]]
            p += 1
            # print(c2)
            if c1 == c2:
                return True
        
        return False
