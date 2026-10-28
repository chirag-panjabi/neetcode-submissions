class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = Counter(chars)
        res = 0
        for word in words:
            w = Counter(word)
            for c in w:
                inC = ch.get(c,0)
                if inC:
                    if w[c] > inC:
                       break
                else:
                    break
            else:
                res += len(word) 
            
        return res