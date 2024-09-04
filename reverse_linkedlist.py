# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #T O(n) linear, MO(1) constant
        prev, curr = None, head #assign pointers

        while curr: #loop through list while curr is not none
            nxt = curr.next #temp store for next node
            curr.next = prev #reversal step
            prev = curr #move prev on step
            curr = nxt #moves loop to next node in list
        return prev #returns prev which is now head of linked list