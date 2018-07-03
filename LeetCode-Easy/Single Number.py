# TIME - O(n)


def singleNumber(arr):
  status = 0
  for num in arr:
    status ^= num
  
  return status
