
# TIME - O(bits)

def binNumberAlternatingBits(num):
  status = n & 1
  n = n >> 1
  while n:
    if n & 1 == status:
      return False
    status = n & 1
    n = n >> 1
  return True
