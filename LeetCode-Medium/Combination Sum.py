# TIME - O(k*(n**k)) k is size of biggest subset


def combinationSum(nums,target):
  
  res = []
  
  def helper(nums,soFar):
    if sum(soFar) == target:
      res.append(soFar)
    else:
      for i in range(len(nums)):
        if nums[i] + sum(soFar) > target : break     
        helper(nums,soFar + [nums[i]])
  
  nums.sort()
  helper(nums,[],target)
