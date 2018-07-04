# TIME - O(n)
# SPACE - O(n)

def maximumBinaryTree(nums):
  
  nodeStack = []
  for num in nums:
    node = TreeNode(num)
    
    while nodeStack and num > nodeStack[-1].data:
      node.left = nodeStack.pop()
    
    if nodeStack:
      nodeStack[-1].right = node
    
    nodeStack.append(node)
  
  return nodeStack[0]
  
