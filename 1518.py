class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        while numBottles>=numExchange:
            newBottle=(numBottles//numExchange) 
            left= numBottles%numExchange
            newBottle=newBottle+left
            numBottles=newBottle
            total= total+numBottles -left
        return total

solve= Solution()
print(solve.numWaterBottles(9,3))        