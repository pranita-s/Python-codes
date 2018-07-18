# TIME - O(h)

#Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

def findClosest(tree,target):
  
  self.gap = float('inf')
  self.closest = float('inf')
  while tree:
    if abs(tree.data - target) < self.gap:
      self.gap = abs(tree.data-target)
      self.closest = tree
    
    if tree.data == target:
      break
    
    if tree.data < target:
      tree = tree.right
    else:
      tree = tree.left
  
  return self.closest.data
      
   
