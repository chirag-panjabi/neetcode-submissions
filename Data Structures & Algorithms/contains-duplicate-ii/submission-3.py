class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window size will be k+1
        if k <= 0:
            return False
        if k >= len(nums):
            k = (len(nums) - 1)  # because window size is k+1, max possible window will be equal to len(nums)

        freq = {}

        # initial window
        for i in range(k + 1):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            # if nums[i] not in freq:
            #     freq[nums[i]] = 1
            # else:
            #     freq[nums[i]] += 1
            if freq[nums[i]] > 1:  # if freq > 1, then its duplicate
                return True

        for high in range(k, len(nums)-1):
            freq[nums[high-k]] -= 1 
            
            if freq[nums[high - k]] == 0:
                del freq[nums[high - k]]
            
            freq[nums[high+1]] = freq.get(nums[high+1], 0) + 1
            
            if freq[nums[high+1]] > 1:  # if freq > 1, then its duplicate
                return True
        
        return False
