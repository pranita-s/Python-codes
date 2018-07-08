# TIME - O(n)


def twoSum(nums,target):
  start, end = 0, len(nums)-1
  while start < end:
    s = nums[start] + nums[end]
    if target > s:
      end -= 1
    elif target < s:
      start += 1
    else:
      return [start+1,end+1]
