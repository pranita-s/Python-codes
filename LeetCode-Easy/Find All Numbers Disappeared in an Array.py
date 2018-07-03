# TIME - O(n)

def findElements(nums):
  
  for num in nums:
    x = abs(num)
    nums[x-1] = -1 * abs(nums[x-1])
    
  return [i+1 for i in range(len(nums)) if nums[i] > 0 ]
  
