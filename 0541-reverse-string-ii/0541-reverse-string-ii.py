class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        n = len(s)
        
        i = 0
        while i < n:
            left = i
            right = min(i + k - 1, n - 1)
            
            # reverse first k characters
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            i += 2 * k
        
        return "".join(s)
