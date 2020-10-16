# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum =[]
        d=0
        
        for x in nums:
            d += x
            sum.append(d)
            
        return sum