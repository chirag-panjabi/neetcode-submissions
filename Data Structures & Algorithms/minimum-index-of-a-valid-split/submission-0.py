from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dominant, count = max(freq.items(), key= lambda x: x[1])

        dom_left = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                dom_left += 1
            if i+1 - dom_left < dom_left:
                if count - dom_left <= (len(nums) - i - 1)//2:
                    return -1
                else:
                    return i
        return -1