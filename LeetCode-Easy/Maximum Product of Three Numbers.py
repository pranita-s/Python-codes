# TIME - O(nlogn)


def maxProduct(nums):
  num.sort()
  return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
