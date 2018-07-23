# TIME - O(n)

def validTriangleNumber(nums): 
  nums.sort(reverse = True)
  result = 0
  for i in range(len(nums)):
    left = i + 1
    right = len(nums)-1
    side1 = nums[left]
    while left < right:
        if nums[left] + nums[right] > side1:
          result += right-left
          left += 1
        else:
          right -= 1
  return result
      
