# TIME - O(2*n+1)

def findDifference(s,t):
  code = 0
  for char in s+t:
    code ^= ord(char)
  
  return chr(code)
