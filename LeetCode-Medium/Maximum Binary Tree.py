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

#########################################################################

def constructMaximumBinaryTree( nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        index = nums.index(max(nums))
        tree = TreeNode(nums[index])
        tree.left = self.constructMaximumBinaryTree(nums[:index])
        tree.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return tree
  
