# TIME - O(n)
# SPACE - O(h)

def binaryTreePaths(root):
  res = []
  
  def helper(root,pathSoFar):
    pathSoFar += str(root.val)
    if not root.left and not root.right:
      res.append(pathSoFar)
    
    if root.left:
      helper(root.left,pathSoFar+'->')
    
    if root.right:
      helper(root.right,pathSoFar+'->')
      
  return res
