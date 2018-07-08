# TIME - O(n)
# SPACE - O(h)

def sumOfLeftLeaves(root):
  stack = [root]
  sumLeft = 0
  while stack:
    node = stack.pop()
    if node.left:
      if not node.left.left and not node.left.right:
        sumLeft += node.left.val
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
 return sumLeft
