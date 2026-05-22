class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap, can't use two pointer here, because need to sort, and if i sort i need to store the index too.
        index = {}
        for i,v in enumerate(nums):
                index[v] = i

        for i in range(len(nums)):
            if target-nums[i] in index:
                if i == index[target-nums[i]]:
                    continue
                return [i, index[target-nums[i]]]
        