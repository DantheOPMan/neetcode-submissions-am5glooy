class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        buckets = [[]for _ in range(len(nums) + 1)]

        for n in counts:
            buckets[counts[n]].append(n)

        res = []
        for b in buckets[::-1]:
            while len(b) > 0:
                res.append(b.pop())
                if len(res) == k:
                    return res

        return res