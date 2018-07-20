# TIME - O(e + q * |V|!) v is number of variables
# SPACE - O(e)


def evaluateDivision(equations, values, queries):
  
  def dfs(n,d,visited):
    if n in lookup and d in lookup[n]:
      return (True, lookup[n][d])    
    for i,v in lookup[n].iteritems():
      if i not in visited:
        visited.add(i)
        tmp = dfs(i,d,visited)
        if tmp[0]:
          return (True,v * tmp[1])
    return (False,0)
    
  lookup = collections.defaultdict(dict)
  for i,e in enumerate(equations):
    lookup[e[0]][e[1]] = values[i]
    if values[i]:
      lookup[e[1]][e[0]] = 1.0/values[i]
  res = []
  for q in queries:
    visited = set()
    tmp = dfs(q[0],q[1],visited)
    res.append(tmp[1] if tmp[0] else -1.0)
  
  return res
