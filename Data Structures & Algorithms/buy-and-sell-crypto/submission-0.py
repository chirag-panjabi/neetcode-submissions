class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        rmax = [0] * n
        maxrt = 0
        
        for i in range(n-1,-1,-1):
            if prices[i] > maxrt:
                maxrt = prices[i]
            rmax[i] = maxrt
        
        mx = 0
        for i in range(n):
            mx = max(mx, rmax[i] - prices[i])

        return mx









