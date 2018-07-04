# TIME - O(n)
# SPACE - O(h)

def binaryTreePruning(root):
  if not root:
    return None
    
  root.left = binaryTreePruning(root.left)
  root.right = binaryTreePruning(root.right)
 
  if not root.left and not root.right and root.val == 0:
    return None
  return root
