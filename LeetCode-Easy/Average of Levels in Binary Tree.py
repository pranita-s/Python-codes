
# TIME - O(n)
# SPACE - O(h)


def avgLevels(root):
  result = []
  level = [root]
  while level:
    sum = 0
    nextLevel = []
    for node in level:
      sum += node.val
      if node.left:
        nextLevel.append(node.left)
      if node.right:
        nextLevel.append(node.right)
      
      result.append(float(sum)//len(level))
      level = nextLevel
   
  return result
    
