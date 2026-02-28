class Solution {
    public boolean isPalindrome(int x) {
        
        // Negative numbers are not palindrome
        if (x < 0) return false;

        int original = x;
        int reversed = 0;

        while (x != 0) {
            int digit = x % 10;        // get last digit
            reversed = reversed * 10 + digit; 
            x = x / 10;               // remove last digit
        }

        return original == reversed;
    }
}