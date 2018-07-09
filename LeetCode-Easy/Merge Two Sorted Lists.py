# TIME - O(n)

def mergeTwoLists(l1,l2):
  dummy = ansHead = ListNode(0)
  
  while l1 and l2:
    if l1.data < l2.data:
      dummy.next = l1
      l1,dummy = l1.next,dummy.next
    else:
      dummy.next = l2
      l2,dummy = l2.next,dummy.next
  #if l1:
  #  dummy.next = l1
  #elif l2:
  #  dummy.next = l2
  dummy.next = l1 or l2
  return ansHead.next
