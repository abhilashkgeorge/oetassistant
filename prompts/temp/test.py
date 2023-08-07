class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        values = []
        lowLimit = 0
        upperLimit = 1

        for i in range( lowLimit, (len(prices) - 1)): #i = 0 , 
            for j in range(upperLimit, (len(prices) - 1)): #j=1, 2
                if prices[i] > prices[j]: # 7 > 1, 
                    lowLimit = j #lowLimit = 1
                    upperLimit = upperLimit + 1 # 2
                else:
                    
                    profit = upperLimit - lowLimit
                    values.append(profit)
                    upperLimit = upperLimit + 1 
                
                
            print(values)

        if lowLimit >= upperLimit: 
            return 0
        else: 
            return max(values)
        

obj = Solution()
prices = [7,1,5,3,6,4]
obj.maxProfit(prices)