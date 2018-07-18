# TIME - O(logn)

def powerOfThree(n):
  
  if n == 0:
    return False
  while n % 3 == 0:
    n /= 3
  
  return n == 1
