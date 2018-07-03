# TIME - O(n)

def maxConsecutiveOnes(arr):
  str_arr = map(str,arr)
  str = ''.join(str_arr)
  return max([len(substring) for substring in str.split('0')])
