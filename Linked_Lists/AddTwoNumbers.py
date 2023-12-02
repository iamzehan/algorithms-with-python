# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=[]
        keep=0
        while l1 and l2: 
            # First we check the constraints
            if l1.next == None and l2.next: # if we ran out of l1, but we still have elements in l2
                l1.next = ListNode() # we expand l1 to match l2
            elif l1.next and l2.next==None: # similarly if we ran out of l2, but we still have elements in l1
                l2.next = ListNode() # we expand l2 to match l1
            add = l1.val + l2.val + keep 
            if add >= 10: #if our sum amounts to 10 or greater
                res.append(add-10) # maximum sum of two single digit numbers is 18, we append 8
                keep = 1 # and keep 1
            else: # if our sum doesn't exceed or equal to 10
                res.append(add) # then we add it as it is and
                keep = 0 # reset our keep to zero
            l1, l2 = l1.next, l2.next # then we move to the next elements in both of our Linked List
        if keep: res.append(keep) # after all the nodes are traverse and we still have a value in our keep,we append it to our result
        return ListNode._array_to_list_node(res) #then convert it to a ListNode and return 


        