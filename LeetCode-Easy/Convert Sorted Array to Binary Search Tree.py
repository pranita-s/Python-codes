# TIME - O(n)


def sortedArrToBST(nums):
  
  
  def helper(nums,start,end):
    if start <= end:
      mid = (start+end)//2
      root = TreeNode(nums[mid])
      root.left = helper(nums,start,mid-1)
      root.right = helper(nums,mid+1,end)
    return root

  return helper(nums, 0 , len(nums)-1)
