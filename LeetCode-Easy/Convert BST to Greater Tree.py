# TIME - O(n)
# SPACE - O(h)

def convertBST(root):
  valSoFar = 0
  def helper(root):
    if not root:
      return 0
    helper(root.right)
    root.val += valSoFar
    valSoFar = root.val
    helper(root.left)
    return root
    
  return helper(root)
  
