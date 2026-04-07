class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # some kind of 2 pointer problem
        best_profit  = 0

        left = 0
        right = 1

        while left < len(prices) and right < len(prices):
            best_profit = max(best_profit, prices[right]-prices[left])
            # if the next value is bigger we should move our right pointer there
            # if its smaller we should move our left pointer there
            if prices[right] < prices[left]: # new smallest number we should try to buy it
                left=right
                right = left + 1
            else:
                right+=1
        return best_profit