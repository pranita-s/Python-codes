# TIME - O(n)
# SPACE - O(h)


def findDiameter(root):
  self.diameter = 0
  def helper(root):
    if not root:
      return 0
    
    left = helper(root.left)
    right = helper(root.right)
    self.diameter = max(self.diameter, left+right)
    
    return(max(left,right)+1)
  
  helper(root)
  return self.diameter
    
