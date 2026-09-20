class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestP = prices[0]
        for p in prices:
            lowestP = min(lowestP, p)
            maxProfit = max(maxProfit, p - lowestP)
        
        return maxProfit
