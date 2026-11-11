class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) !=1 :
            if not stones:
                return 0
            x= heapq.heappop_max(stones)
            y= heapq.heappop_max(stones)
            if x == y:
                continue
            else:
                mi = min(x,y)
                ma = max(x,y)
                heapq.heappush_max(stones, ma-mi)
        
        return stones[0]