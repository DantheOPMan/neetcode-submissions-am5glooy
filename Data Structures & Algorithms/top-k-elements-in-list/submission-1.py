class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for n in nums:
            data[n] = data.get(n,0) + 1
        for n, c in data.items():
            buckets[c].append(n)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res