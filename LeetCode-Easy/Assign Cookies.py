# TIME - O(n)

def findContentChildren(g,s):
  g.sort()
  s.sort()
  i,j,count = 0,0,0
  while i < len(g) and j < len(s):
    if g[i] <= s[j]:
      i+=1
      j+=1
      count+=1
    else:
      j+=1
  return count
