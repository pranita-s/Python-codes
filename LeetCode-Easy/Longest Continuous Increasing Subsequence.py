# TIME - O(n)


def findLengthOfLCIS(nums):
  count = 1
  result = 0
  for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
      count += 1
      result = max(result,count)
    else:
      count = 1
  
  return result
