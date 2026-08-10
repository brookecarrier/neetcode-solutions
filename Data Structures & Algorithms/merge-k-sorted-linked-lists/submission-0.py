# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        curr = ListNode(0)
        dummy = curr # at the end return dummy.next

        while lists:
            # find list w smallest head val
            minIdx = 0
            for i in range(len(lists)):
                if lists[i].val < lists[minIdx].val:
                    minIdx = i

            curr.next = lists[minIdx]
            curr = curr.next
            lists[minIdx] = lists[minIdx].next

            if lists[minIdx] == None:
                lists.pop(minIdx)
                        
        return dummy.next



        