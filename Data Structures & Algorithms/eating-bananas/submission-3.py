class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            total = 0
            m = l + (r - l) // 2
            for p in piles:
                total += math.ceil(float(p) / m)

            if total <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
