# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = l1
        number1 = ''
        while nextNode.next != None:
            print(nextNode.val)
            number1 = str(nextNode.val) + number1
            nextNode = nextNode.next
        print(nextNode.val)      
        number1 = str(nextNode.val) + number1        
        print(number1)
        
        nextNode = l2
        number2 = ''
        while nextNode.next != None:
            print(nextNode.val)
            number2 = str(nextNode.val) + number2
            nextNode = nextNode.next
        print(nextNode.val)      
        number2 = str(nextNode.val) + number2       
        print(number2)
        sum = int(number1) + int(number2)
        sum = str(sum)
        print(sum)
        totalLength = len(sum)
        nodeList = ListNode(0, None)
        for i in range(totalLength):
            currentNode=
            position = (totalLength - 1 - i)
            node = ListNode()