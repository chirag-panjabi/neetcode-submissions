class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store: { number: index }
        seen = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            # If the complement exists in our map, we found the pair
            if diff in seen:
                return [seen[diff], i]
            
            # Otherwise, store the current number and its index
            seen[num] = i