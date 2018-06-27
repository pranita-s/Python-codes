# TIME = O(number of bits)



def hammingDist(n,m):
  xor = n^m
  count = 0
  while xor:
    count += (xor & 1)
    xor >>= 1
  return count
