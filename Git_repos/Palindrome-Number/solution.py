from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine if an integer is palindrome without using extra space or string conversion.
        
        Approach Ideas:
        - Handle negative numbers (immediate false)
        - Reverse the number mathematically
        - Compare reversed with original
        
        Edge Cases:
        - Negative numbers
        - Numbers ending with 0 (except 0 itself)
        - Single digit numbers
        """
        # TODO: Implement the solution here
        pass


# For local testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))    # Expected: True
    print(sol.isPalindrome(-121))   # Expected: False
    print(sol.isPalindrome(10))     # Expected: False