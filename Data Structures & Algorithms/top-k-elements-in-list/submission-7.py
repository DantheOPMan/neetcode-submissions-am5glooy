class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        data = {}
        for n in nums:
            data[n] = data.get(n,0) + 1

        buckets = [[]for _ in range(len(nums) + 1)]

        for n in data:
            buckets[data[n]].append(n)

        res = []
        for bucket in reversed(buckets):
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res

        return res