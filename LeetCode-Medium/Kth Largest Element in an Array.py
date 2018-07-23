# TIME - O(n) ~ O(n**2)
# SPACE - O(1)

import random
def kthLargest(nums,k):
  
  def partitionAroundPivot(left,right,pivot):
    pivot_val = nums[pivot]
    nums[pivot], nums[right] = nums[right], nums[pivot]
    new_pivot_index = left
    for i in range(left,right):
      if nums[left] > pivot_val:
        nums[left], nums[new_pivot_index] = nums[new_pivot_index],nums[left]
        new_pivot_index += 1
    
    nums[new_pivot_index], nums[right] = nums[right], nums[new_pivot_index]
    return new_pivot_index
  
  left,right = 0, len(nums)-1
  while left<right:
    old_pivot_index = random.randint(left,right)
    pivot_index = partitionAroundPivot(left,right,old_pivot_index)
    if pivot_index == k-1:
      return nums[pivot_index]
    if pivot_index > k:
      right = pivot_index - 1
    else:
      left = pivot_index + 1
  
