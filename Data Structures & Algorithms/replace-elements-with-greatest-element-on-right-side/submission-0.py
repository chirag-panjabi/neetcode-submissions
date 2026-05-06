class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # this is the result of trial and error, not solid understanding
        # if i were asked do it again, it will take me lot of time
        maxSuffix = [-1]*len(arr)
        mx = 0
        last = len(arr)-1
        for i in range(last, -1, -1):
            if i != last:
                maxSuffix[i] = mx
            mx = arr[i] if arr[i]>mx else mx
        return maxSuffix





