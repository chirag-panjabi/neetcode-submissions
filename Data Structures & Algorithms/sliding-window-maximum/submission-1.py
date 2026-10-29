class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # win = deque()
        win = {}
        mx = float('-inf')
        sm = float('-inf')
        res = []
        p = 0
        for i in range(k):
            # win.append(nums[i])
            win[nums[i]] = win.get(nums[i], 0) + 1
            mx = max(mx, nums[i])
            sm = nums[i] if nums[i] < mx and nums[i] > sm else sm
        res.append(mx)
        # print(mx, sm)
        for i in range(k, len(nums)):
            # win.append(nums[i])
            # win.popleft()
            
            win[nums[i]] = win.get(nums[i], 0) + 1
            win[nums[p]] -= 1
            if win[nums[p]] == 0:
                del win[nums[p]]
            p += 1

            if mx not in win: # o(n)
                print(sm)
                if sm not in win: # o(n) -> use hashmap
                    mx = max(win)
                else:
                    mx = max(sm, nums[i])
                    sm = nums[i] if nums[i] < mx and nums[i] > sm else sm
            else:
                mx = max(mx, nums[i])
                sm = nums[i] if nums[i] < mx and nums[i] > sm else sm
            res.append(mx)
        
        return res