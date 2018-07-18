# TIME - O(n)

def removeElement(nums,target):
  start,end = 0, len(nums)-1
  while start <= end:
    if nums[start] == target:
      nums[start],nums[end],end = nums[end],nums[start],end-1
    else:
      start += 1
  return start