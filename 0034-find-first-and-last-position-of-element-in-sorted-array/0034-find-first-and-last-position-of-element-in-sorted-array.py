class Solution:
    def searchRange(self, nums, target):
        
        n = len(nums)
        left, right = 0, n - 1
        first = -1
        
        # Find First Position
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
                
            if nums[mid] == target:
                first = mid
        
        left, right = 0, n - 1
        last = -1
        
        # Find Last Position
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
            if nums[mid] == target:
                last = mid
        
        return [first, last]