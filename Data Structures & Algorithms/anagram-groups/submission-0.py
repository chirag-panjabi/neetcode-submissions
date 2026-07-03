from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            freq = Counter(s)
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        ans = []
        for val in anagrams.values():
            ans.append(val)
        return ans