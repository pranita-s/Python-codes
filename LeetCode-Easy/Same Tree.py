# TIME - O(n)


def sameTree(p,q):
  
  if not p and not q:
    return True
  if p and q and p.val == q.val:
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)
  else:
    return False
  
