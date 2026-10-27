class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        n = len(s)
        res = []
        while j < n:
            i = j
            while s[j] != '#' and j<n:
                j += 1
            lenstr = int(s[i:j])
            skip = len(str(lenstr)) + 1
            i = i + skip
            j += lenstr + 1
            res.append(s[i:j])
             
        return res

