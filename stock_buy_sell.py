#In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout the day are represented in the form of an array of prices. 
#Given an array price of size n, find out the maximum profit that a share trader could have made.

class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        
        profit=n*[0]
        
        max_pro=price[n-1]
        for i in range(n-2,-1,-1):
            max_pro=max(max_pro,price[i])
            profit[i]=max(profit[i+1],max_pro-price[i])
            
        res=0
        min_pro=price[0]
        for i in range(1,n):
            min_pro=min(min_pro,price[i])
            res=max(res,profit[i]+ (price[i]-min_pro))
        
        return res
