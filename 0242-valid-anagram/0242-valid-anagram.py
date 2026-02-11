class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        
        i = 0
        while i < len(s):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            i += 1
        
        # check if all counts are zero
        for num in count:
            if num != 0:
                return False
        
        return True
