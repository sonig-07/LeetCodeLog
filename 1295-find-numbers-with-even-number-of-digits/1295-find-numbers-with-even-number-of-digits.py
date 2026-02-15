class Solution:
    def findNumbers(self, nums):
        count_even = 0
        
        for num in nums:
            digits = 0
            temp = num
            
            while temp > 0:
                digits += 1
                temp //= 10
            
            if digits % 2 == 0:
                count_even += 1
        
        return count_even
