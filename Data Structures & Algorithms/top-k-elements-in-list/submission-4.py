class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for n in nums:
            data[n] = data.get(n,0) + 1
        buckets = [[] for i in range(len(nums)+1)]
        for n in data:
            buckets[data[n]].append(n)

        res = []
        for i in range(len(buckets)-1,0,-1):
            x = 0
            while len(buckets[i]) > x:
                res.append(buckets[i][x])
                x+=1
                if len(res) == k:
                    return res

