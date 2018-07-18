# TIME - O(logn)

def powerOfThree(n):  
  if n == 0:
    return False
  while n % 3 == 0:
    n /= 3  
  return n == 1


# TIME - O(1)

import math
def powerofThree2(n):
    return n > 0 and (math.log10(n)/math.log10(3)).is_integer()
