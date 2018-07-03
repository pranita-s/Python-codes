# TIME - O(n)

def invertBinaryTree(root):
  if not root:
    return None
  
  left = invertBinaryTree(root.left)
  right = invertBinaryTree(root.right)
  
  root.left,root.right = right, left
  
  return root
