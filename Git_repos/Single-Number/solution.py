from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Use XOR property:
        a ⊕ a = 0
        a ⊕ 0 = a
        XOR is commutative and associative
        
        So all pairs cancel out → only single remains
        """
        # TODO: Initialize result = 0
        # TODO: For each num in nums → result ^= num
        # TODO: Return result
        pass