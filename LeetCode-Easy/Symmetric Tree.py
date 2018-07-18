# TIME - O(n)
# SPACE - O(h)
# RECURSIVE

def SymmetricTree(root):
  def helper(node1,node2):
    if not node1 and not node2:
      return True
    if not node1 or not node2 or node1.data != node2.data:
      return False
    return helper(node1.left,node2.right) and helper(node1.right,node2.left)
  
  if not root:
    return False
  return helper(root.left,root.right)
  
  
# TIME - O(n)
# SPACE - O(widthOfTree)

def SymmetricTree(root):
  if not root:
    return True
  s = []
  s.append(root.left)
  s.append(root.right)
  
  while s:
    p, q = s.pop(), s.pop()
    if not p and not q:
      continue
    if not p or not q or not p.data == q.data:
      return False
    s.append(p.left)
    s.append(q.right)
    s.append(p.right)
    s.append(p.left)
  
  return True
  

