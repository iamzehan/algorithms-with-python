# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        li = head
        while li:
            li = li.next
            size+=1
        index = size - n
        res = []
        position = 0
        while head:
            if (position!=index):
                position += 1
                res.append(head.val)
                head = head.next
            else:
                position+=1
                head = head.next
        return ListNode._array_to_list_node(res)