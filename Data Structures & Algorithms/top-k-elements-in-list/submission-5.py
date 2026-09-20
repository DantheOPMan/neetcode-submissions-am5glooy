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
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
