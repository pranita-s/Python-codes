# TIME - O(q + r)
# SPACE - O(q + r)

import collections
def loudAndRich(richer,quiet):
  
  def dfs(start,result):
    if result[start] == None:
      result[start] = start
      for neighbor in g[start]:
        smallest_number = dfs(neighbor, result)
        if quiet[smallest_number] < quiet[start]:
          result[start] = neighbor    
    return result[start] 
  
  g = collections.defaultdict(list)
  for i,j in richer:
    g[j].append(i)
  
  res = []
  
  for i in range(quiet):
    dfs(i,res)
