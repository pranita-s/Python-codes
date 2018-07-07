# TIME - O(n)

def maxCount(m, n , ops):
  if not ops:
    return m * n
  
  minStart = sys.maxsize
  maxEnd = sys.maxsize
  
  for o in ops:
            minStart = min(minStart,o[0])
            minEnd = min(minEnd,o[1])
        return minStart*minEnd
