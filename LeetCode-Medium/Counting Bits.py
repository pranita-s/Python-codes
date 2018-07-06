# TIME - O(n)

def countingBits(n):
  result = [0]
  for i in range(1,n+1):
    result.append((i&1) + result[i >> 1])
  
  return result
