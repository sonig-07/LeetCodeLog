class Solution:
    def twoSum(self, nums, target):
        seen = {}
        
        i = 0
        for num in nums:
            needed = target - num
            
            if needed in seen:
                return [seen[needed], i]
            
            seen[num] = i
            i += 1
