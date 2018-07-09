# TIME - O(n)
# SPACE - O(h)

import collections
def levelOrderBottom(root):
  
  res , q = [], collections.deque([root,0])
  
  while q:
    curr,level = q.popleft()
    if curr:
      if len(res) < level + 1:
        res.insert(0, [])
      res[-(level+1)].append(curr.val)
      q.append([curr.left,level+1])
      q.append([curr.right,level+1])
  
  return res
    
