# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # If one list is empty,
        # return the other list directly
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # Dummy/sentinel node helps simplify logic
        dummy = node = ListNode()

        # Compare nodes from both lists
        # and attach smaller node to merged list
        while list1 and list2:

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            # Move pointer forward in merged list
            node = node.next

        # Attach remaining nodes
        # Only one of them will exist
        node.next = list1 or list2

        # Return merged list starting after dummy node
        return dummy.next


    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        # Edge case:
        # If input list is empty
        if not lists:
            return None

        # Keep merging lists in pairs
        # until only one final merged list remains
        while len(lists) > 1:

            mergedLists = []

            # Merge lists two at a time
            for i in range(0, len(lists), 2):

                # First list
                l1 = lists[i]

                # Second list if it exists,
                # otherwise None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge the two sorted lists
                mergedLists.append(self.mergeTwoLists(l1, l2))

            # Update lists with newly merged lists
            lists = mergedLists

        # Final fully merged list
        return lists[0]