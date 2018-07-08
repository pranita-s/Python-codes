# TIME - O(n ** 2)
# SPACE - O(n)

def numBoomerangs(points):
  res = 0
  for p in points:
    d = {}
    for q in points:
      x = p[0] - q[0]
      y = p[1] - q[1]
      d[x*x + y*y] = 1 + d.get((x*x + y*y),0)
    
    for key in d:
      res += d[key] * (d[key]-1)
  
  return res
