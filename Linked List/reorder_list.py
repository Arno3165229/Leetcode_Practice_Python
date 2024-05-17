# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ## stack solution
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head

        dummyNode = ListNode()
        slow = dummyNode
        fast = dummyNode
        dummyNode.next = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        stack = []
        while second:
            stack.append(second)
            second = second.next

        while head and stack:
            tmp_head = head.next
            second = stack.pop()
            head.next = second
            second.next = tmp_head
            head = tmp_head
        
        return head