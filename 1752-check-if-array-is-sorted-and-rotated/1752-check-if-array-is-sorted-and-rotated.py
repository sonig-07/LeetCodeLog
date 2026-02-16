class Solution:
    def check(self, nums):
        count = 0
        n = len(nums)
        
        i = 0
        while i < n:
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            i += 1
        
        return count <= 1
