# TIME - O(n)

def missingNumber(nums):
  l = len(nums)
  total = l * (l + 1)//2
  for num in nums:
    total -= num
  return total
