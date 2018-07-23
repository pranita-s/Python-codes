# TIME - O(k * C(n,k))
# SPACE - O(k)


def combinations(n,k):  
  
  nums = range(1,n+1)  
  
  def helper(nums,soFar,k,curr):
    if k == 0:
      res.append(soFar)    
    for i in range(curr+1,n):
      helper(nums,soFar + [nums[i],k-1,i)
   
  res = []
  helper(nums,soFar,k,0)
