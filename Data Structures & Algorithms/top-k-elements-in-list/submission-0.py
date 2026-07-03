
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)        
        # Bucket: index = frequency, value = list of nums with that frequency
        
        freq_bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            freq_bucket[freq].append(num)

        print(freq_bucket)
        res = []
        for i in range(len(freq_bucket)-1,-1,-1):
            if k <= 0:
                return res
            if freq_bucket[i]:
                for v in freq_bucket[i]:
                    res.append(v)
                k -= len(freq_bucket[i])
            

