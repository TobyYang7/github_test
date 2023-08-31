# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addtwoNumbers(self, l1, l2):
        carry = 0
        add_bit = 0
        sum = l1.val+l2.val+carry
        res = ListNode()

        while (l1.next and l2.next):
            if (sum >= 10):
                add_bit = sum-10
                carry = 1
            else:
                add_bit = sum
                carry = 1
            res.val = sum
            res = res.next
            l1 = l1.next
            l2 = l2.next

        return res
