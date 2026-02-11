class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        i = 1
        while i < len(prices):
            
            # If we find a lower price, update minimum
            if prices[i] < min_price:
                min_price = prices[i]
            
            # Calculate profit if sold today
            else:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
            
            i += 1
        
        return max_profit
