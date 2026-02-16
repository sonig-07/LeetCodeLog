class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        
        arr[0] = 1
        
        i = 1
        while i < len(arr):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
            i += 1
        
        return arr[-1]
