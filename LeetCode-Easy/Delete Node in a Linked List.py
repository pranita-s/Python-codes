# TIME - O(1)

def deleteNode(node):
  node.val = node.next.val
  node.next = node.next.next
