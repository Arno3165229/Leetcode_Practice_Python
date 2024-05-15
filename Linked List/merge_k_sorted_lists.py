# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # if lists == None: ## which means lists = [[]]
        #     return None
        
        if not lists or len(lists) == 0: ## Both handling empty list case -> lists = []
            return None

        mergedKList = []

        while len(lists) != 1:
            for i in range(0, len(lists), 2):
                mergedKList.append(self.mergeTwoLists(lists[i], lists[i+1])) if (i+1) < len(lists) else mergedKList.append(lists[i])
            lists = mergedKList
            mergedKList = []

        return lists[-1]
    
    def mergeTwoLists(self, list1, list2):
        if list1 == None: return list2
        if list2 == None: return list1

        dummyNode = ListNode()
        prev = dummyNode
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                prev.next = cur1
                prev = cur1
                cur1 = cur1.next
            else:
                prev.next = cur2
                prev = cur2
                cur2 = cur2.next

        if cur1: prev.next = cur1
        else: prev.next = cur2

        return dummyNode.next
