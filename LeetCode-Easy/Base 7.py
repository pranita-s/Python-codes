# TIME - O(1)
# SPACE - O(1)


def baseSeven(n):
  if n == 0:
    return '0'
  result = ''
  while n:
    result = str(n % 7) + result
    n /= 7
  
  return result if n > 0 else '-'+result
