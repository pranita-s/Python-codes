# TIME - O(n)
# SPACE - O(h)


def findSecondMinimumValue(self,root):
  
  self.secondMin = float('inf')
  def helper(node):
    if not node:
      return 
    if node.val > self.secondMin:
      return 
    elif root.val < node.val < self.secondMin:
      self.secondMin = node.val
    
    helper(node.left)
    helper(node.right)
  
  helper(root)
  return self.secondMin
