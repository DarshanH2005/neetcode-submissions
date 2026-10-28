# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # create a gap of n + 1 nodes
        for _ in range(n + 1):
            fast = fast.next

        # move both together
        while fast:
            slow = slow.next
            fast = fast.next

        # bypass the node to remove
        slow.next = slow.next.next

        return dummy.next