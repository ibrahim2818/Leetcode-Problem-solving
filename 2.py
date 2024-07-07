# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1= int(l1.reverse())
        l2= int(l2.reverse())
        l3= l1+l2
        l3= list(str(l3.reverse()))
        return l3
myob= Solution()
print(myob.addTwoNumbers([2,4,3],[5,6,4]))
        