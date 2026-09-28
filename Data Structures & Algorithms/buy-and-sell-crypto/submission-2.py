class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # min_price = prices[0]

        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)

        # return max_profit

        max_profit = 0
        l, r = 0, 1
        
        while r != len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit