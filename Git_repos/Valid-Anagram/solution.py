class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Two approaches:
        1. Sorting: O(n log n)
        2. HashMap/Count array: O(n) - better
        
        Since only lowercase letters, we can use array of size 26
        """
        # TODO: First check if len(s) != len(t) → return False
        # TODO: Create count = [0] * 26
        # TODO: For each char in s → count[char - 'a'] += 1
        # TODO: For each char in t → count[char - 'a'] -= 1
        # TODO: Check if all counts == 0
        pass