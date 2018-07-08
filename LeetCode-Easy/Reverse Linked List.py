# TIME - O(n)

def reverseLL(head):
  dummy = ListNode(0)
  while head:
    dummy.next, head.next, head  = head, dummy.next, head.next
  
  return dummy.next
