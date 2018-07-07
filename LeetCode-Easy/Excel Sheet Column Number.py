# TIME - O(n)


def titleToNumber(s):
  col = 0
  for i, c in enumerate(reversed(s)):
    col += (26**i) * (ord(c) - ord('A')+1)
  
  return col
