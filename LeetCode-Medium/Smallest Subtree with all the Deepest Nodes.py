
# TIME - O(n)
# SPACE - O(h)

import collections
def smallestSubtree(root):
  result = collections.namedtuple('result',('node','depth'))
  
  def dfs(node):
    if not node:
      return result(None,0)
    
    left, right = dfs(node.left), dfs(node.right)
    if left.depth > right.depth:
      return result(left.node, left.depth+1)
    if left.depth < right.depth:
      return result(right.node, right.depth+1)
    return result(node, left.depth+1)
  
  return dfs(root).node
  
  
# TIME - O(n)
# SPACE - O(n)

def subtreeWithAllDeepest(root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def findLCA(root,nodes):
            status = collections.namedtuple('status',('count','ancester'))
            def helper(root):
                if not root:
                    return status(0,None)
                
                left = helper(root.left)
                if left.count == len(nodes):
                    return left
                right = helper(root.right)
                if right.count == len(nodes):
                    return right
                
                cnt = left.count + right.count + int(root in nodes)
                return status(cnt,root)
            
            return helper(root).ancester
        
        
        lookup = {}
        self.maxD = 0
        def findDepths(root,d):
            if not root:
                return None
            self.maxD = max(self.maxD,d)
            lookup[d].append(root)
            findDepths(root.left,d+1)
            findDepths(root.right,d+1)
        
        lookup = collections.defaultdict(list)
        findDepths(root,0)
        
        return findLCA(root,lookup[self.maxD])
  
