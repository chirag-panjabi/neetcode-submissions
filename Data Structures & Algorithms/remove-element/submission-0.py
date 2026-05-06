class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val : # i should not be last element
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
                        k += 1
                        break
            else: 
                k += 1
            
        return k
