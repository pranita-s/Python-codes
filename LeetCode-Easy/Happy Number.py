# TIME - O(k) k steps to happy number
# SPACE - O(k)


def happyNumber(n):
  
  def splitted(n):
    res = []
    while n:
      res.append(n%10)
      n //= 10
    return res
    
  lookup = {}
  while n!=1 and n not in lookup:
    digits = splitted(n)
    temp = 0
    for d in digits:
      temp += d*d
    n = temp
  
  return n == 1
