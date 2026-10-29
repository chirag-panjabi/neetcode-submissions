class Solution:
    def trap(self, height: List[int]) -> int:
        # stk = []
        water = 0
        c = 0
        cur_mx = 0
        sub = 0
        index_cur_mx = 0
        for i, v in enumerate(height):
            if cur_mx <= v:
                water += cur_mx * c - sub
                cur_mx = v
                index_cur_mx = i
                c = 0
                sub = 0
            else:
                sub += v
                c += 1
        
        c = 0
        cur_mx = 0
        sub = 0
        
        for i in range(len(height)-1, index_cur_mx-1, -1):
            v= height[i]
            if cur_mx <= v:
                water += cur_mx * c - sub
                cur_mx = v
                c = 0
                sub = 0
            else:
                sub += v
                c += 1
        
        return water
        
