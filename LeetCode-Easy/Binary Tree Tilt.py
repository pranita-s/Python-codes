# TIME - O(n)
# SPACE - O(h)

def findTilt(self,root):
  self.tilt = 0
  
  def helper(root):
    if not root:
      return 0
      
    left = helper(root.left)
    right = helper(root.right)    
    self.tilt += abs(left-right)   
    return(root.val+left+right)
  
  helper(root)
  return self.tilt
