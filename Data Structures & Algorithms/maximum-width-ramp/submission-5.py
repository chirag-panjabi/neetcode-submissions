class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, v in enumerate(nums):
            if not stack or nums[stack[-1]] > v:
                stack.append(i)


        mx = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                mx = max(mx, j - stack.pop())

        return mx