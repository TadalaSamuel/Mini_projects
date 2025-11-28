from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two pointers:
        - slow: position to place next non-zero
        - fast: explore array
        
        After placing all non-zeros, fill rest with 0
        """
        # TODO: Initialize slow = 0
        # TODO: Loop fast from 0 to len(nums)-1
        # TODO: If nums[fast] != 0 → swap with slow and slow += 1
        # TODO: After loop, fill nums[slow:] with 0s
        pass
    