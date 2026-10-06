class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        p = 0
        for i in arr:
            if len(res) < k:
                res.append(i)
                continue
            if abs(x-i) < abs(x-res[p]):
                res.append(i)
                p += 1
            elif abs(x-i) == abs(x-res[p]):
                if res[p] < i:
                    break
                else:
                    res.append(i)
                    p += 1
            else:
                break
        return res[p:]