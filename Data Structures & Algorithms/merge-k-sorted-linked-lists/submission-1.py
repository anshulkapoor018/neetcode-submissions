# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        dummy = node = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2

        return dummy.next
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        dummy = ListNode()

        while len(lists) > 1:
            list1 = lists.pop()
            list2 = lists.pop()

            mergedList = self.mergeTwoLists(list1, list2)

            lists.append(mergedList)
        
        return lists[0]


