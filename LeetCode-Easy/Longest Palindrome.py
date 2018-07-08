# TIME - O(n)
# SPACE - O(n)


def longestPalindrome(s):
  d = {}
  for c in s:
    d[c] = d.get(c,0) + 1
    
  
  numOdds = 0
  for c in s:
    if d[c] % 2:
      numOdds += 1
  
  return len(s) - numOdds + int(numOdds > 0)
  
  
