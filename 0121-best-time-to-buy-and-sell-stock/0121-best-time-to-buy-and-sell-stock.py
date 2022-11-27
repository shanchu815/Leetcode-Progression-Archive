class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_date = 0
        sell_date = 1
        max_profit = 0
        dates = len(prices)
        
        while sell_date < dates: 
#before the week is up

            if prices[buy_date] < prices[sell_date]:
                curr_profit = prices[sell_date] - prices[buy_date]
                max_profit = max(max_profit, curr_profit)
#get the profit and compare to the max
            
            else:
                buy_date = sell_date
#if it is not profitable
#that means the price on sell_date is lower than on buy_date
#so it's cheaper to buy it on that date instead

            sell_date += 1
#we already checked this date, check tomorrow if it's lower/higher

        return max_profit