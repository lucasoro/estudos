# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         head = l3 = Node(0)
#         carry = 0

#         while l1 or l2 or carry:
            
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
            
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next

#             l3.val = carry % 10
#             carry = carry // 10

#             if l1 or l2 or carry:
#                 l3.next = Node(0)
#                 l3 = l3.next
        
#         return head


# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, l1, l2):
        
        

list1 = Solution()
print(list1.addTwoNumbers([Node(203), Node(400)))