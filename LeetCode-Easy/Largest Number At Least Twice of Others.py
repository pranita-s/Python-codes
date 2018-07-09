# TIME - O(n)


def dominantIndex(nums):
  first, second , index = -1,-1,0
  for  i,num in enumerate(nums):
    if num > first:
      first = num
      second = first
      index = i
    elif num > second:
      second = num
  if first > second*second:
    return index
  else:
    return -1
