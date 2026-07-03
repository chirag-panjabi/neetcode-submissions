class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        j = 0
        while j < len(s):
            while s[j]!= '#':
                j += 1
            str_len = int(s[i:j])
            j += 1
            res.append( s[ j : j + str_len ] )
            i = j + str_len
            j = i
        return res


