class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Bit trick: n & (n-1) == 0
        Only works if n > 0 and is power of 2
        
        Reason: 8 (1000) & 7 (0111) = 0
        """
        # TODO: Handle n <= 0 → return False
        # TODO: Return (n & (n - 1)) == 0
        pass