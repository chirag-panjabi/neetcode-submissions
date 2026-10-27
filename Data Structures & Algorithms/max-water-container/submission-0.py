class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        water = 0
        mx = 0
        while l < r:
            hl = heights[l]
            hr = heights[r]
            area = min(hl,hr) * (r-l)
            mx = max(mx, area)
            if hl < hr:
                l += 1
            else:
                r -= 1
        return mx