from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next != None:
            return str(self.val) + " " + str(self.next)
        else:
            return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum = l1.val + l2.val
        overflow = 1 if sum > 9 else 0  # if sum is greater than 9
        sum = sum % 10 if overflow else sum  # save the right digit
        l1.val = sum

        if l1.next == None and l2.next == None:
            l1.next = ListNode(overflow) if overflow else None
        elif l1.next == None:
            l1.next = self.addTwoNumbers(
                l2.next, ListNode(overflow)) if overflow else l2.next
        elif l2.next == None:
            l1.next = self.addTwoNumbers(
                l1.next, ListNode(overflow)) if overflow else l1.next
        else:
            l2.next.val += overflow
            l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1


s = Solution()
list1 = ListNode(9, ListNode(9, ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
list2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

print(s.addTwoNumbers(list1, list2))
