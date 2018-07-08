# TIME - O(n)
# SPACE - O(h)


def minDiff(self,root):
  self.minimum = float('inf') 
  self.previous = float('inf')
  def inorder(root):
    if root:
      inorder(root.left)
      self.minimum = min(self.minimum, root.val - self.previous)
      self.previous = root.val
      inorder(root.right)
    
  inorder(root)
  return self.minimum
