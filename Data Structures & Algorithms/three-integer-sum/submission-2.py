class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    while j > 0 and j < n and nums[j] == nums[j-1]:
                        j += 1
                    while k >= 0 and k < n-1 and nums[k] == nums[k+1]:
                        k -= 1
            
            i += 1

        return res

