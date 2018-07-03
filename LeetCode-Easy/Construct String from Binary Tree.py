# TIME - O(n)

def binaryStringFromTree(tree):
  
  if not tree:
    return ''
  
  left = binaryStringFromTree(tree.left)
  right = binaryStringFromTree(tree.right)
  val = str(tree.val)
  if left == '' and right == '':
    return val
  elif right == '':
    return val + '(' + left + ')'
  else:
    return val + '(' + left + ')' + '(' + right + ')'
