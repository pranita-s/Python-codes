# TIME - O(n**4)
# SPACE - O(n)

def ambiguousCoordinates(s):
  
  def addpunc(s):
    if len(s) == 0: return []
    if len(s) == 1: return [s]
    res = []
    if s[-1] == '0':
      res = []
    if s[0] == '0':
      res = ["%s.%s"%(s[0],s[1:])]
    else:
      for i in range(1,len(s)):
        res.append("%s.%s"%(s[:i],s[i:]))
    if s[0] != '0':
      res.append(s)
    return res
  
  result = []
  s = s[1:-1]
  for i in range(1,len(n)):
    left,right = addpunc(s[:i]), addpunc(s[i+1:])
    for i in left:
      for j in right:
        result.append("(%s,%s)"%(i,j))
  return result
  
