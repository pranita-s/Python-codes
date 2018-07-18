# TIME - O(1)

def powerOfTwo(n):
  
  if n != 0 and n & (n-1) == 0:
    return True
  else:
    return False
