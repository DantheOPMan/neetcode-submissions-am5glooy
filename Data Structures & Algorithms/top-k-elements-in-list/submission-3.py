class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dataMap = {}
        for n in nums:
            dataMap[n] = dataMap.get(n,0) +1

        bucket = [[]for _ in range(len(nums)+1)]
        print(bucket)
        for n in dataMap:
            bucket[dataMap[n]].append(n)

        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return False