class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = {'W':0,'B':0}
        l = 0
        for i in range(k):
            freq[blocks[i]] += 1
        
        r = k
        mi = freq['W']
        while r <len(blocks):
            freq[blocks[r]] += 1
            freq[blocks[l]] -= 1
            mi = min(mi, freq['W'])
            l += 1
            r += 1
        
        return mi