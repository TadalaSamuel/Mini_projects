# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Use dummy node + pointer approach.
        Compare nodes and attach smaller one.
        """
        # TODO: Create dummy = ListNode()
        # TODO: tail = dummy
        # TODO: While both lists not null
        # TODO: Attach remaining list at end
        # TODO: Return dummy.next
        pass