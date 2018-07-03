
# TIME - O(n)
# SPACE - O(h)


def trim(root,L,R):
  
  if not root:
    return None
  
  if root.val < L:
    return trim(root.right,L,R)
  
  if root.val > R:
    return trim(root.left,L,R)
  
  root.left = trim(root.left,L,R)
  root.right = trim(root.right,L,R)
  
  return root
