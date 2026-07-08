class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for i in range(0,len(prices)):
            min_price=min(prices[i],min_price)
            profit=prices[i]-min_price
            max_profit=max(max_profit,profit)
        return max_profit