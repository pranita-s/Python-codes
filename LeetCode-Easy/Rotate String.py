# TIME - O(m + n)
# SPACE - O(n)

def createLookupTable(s):
  lookup = [0] * len(s)
  j = 0
  for i in range(1,len(s)):
    if s[j] == s[i]:
      lookup[i] = j + 1
      j += 1
      i += 1
    else:
      if j == 0:
        i += 1
      else:
        j = lookup[j-1]
 
 return lookup
      

def KMP(str,substring):
  lookup = createLookupTable(substring)
  i , j = 0, 0
  while i < len(str) and j < len(substring):
    if s[i] == s[j]:
      i += 1
      j += 1
    else:
      if j == 0:
        i += 1
      else:
        j = lookup[j-1]
    if j == len(substring):
      return True
  
  return False

def rotateString(s,t):
  if len(s) != len(t):
    return False
  
  return KMP(s+s,t)

############################################################################

def rotateString(A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        S = A+A
        #return S
        if len(A) != len(B):
            return False
        else:
            if B in S:
                return True
            else:
                return False
            
