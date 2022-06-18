import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0, None)
        ll1 = l1
        ll2 = l2
        current = dummy_head
        carry = 0

        while ((ll1 != None) or (ll2 != None)):
            x = 0
            y = 0
            if (ll1 != None):
                x = ll1.val
            if (ll2 != None):
                y = ll2.val

            sum = carry + x + y
            carry = sum/10
            current.next = ListNode((sum % 10), None)
            current = current.next
            if ll1 != None:
                ll1 = ll1.next
            if ll2 != None:
                ll2 = ll2.next
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next