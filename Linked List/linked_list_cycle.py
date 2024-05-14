# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        
        slow = head
        fast = head

        ## while slow.next and fast.next.next: ## fast.next might be None -> fast.next.next will get error
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False