# TIME - O(max_n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def merge(tree1,tree2):
  if not tree1 and not tree2:
    return None
  ans = TreeNode((tree1.val if tree1 else 0)+(tree2.val if tree2 else 0))
  ans.left = merge(tree1.left,tree2.left)
  ans.right = merge(tree1.right,tree2.right)
  return ans
