class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]
        for n in prices:
            lowest = min(lowest, n)
            maxProfit = max(maxProfit, n - lowest)

        return maxProfit