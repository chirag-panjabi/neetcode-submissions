class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                sums.append(cur_sum)
        sums.sort()

        res = 0
        for i in range(left - 1, right):
            res += sums[i]

        return res % 1000000007


