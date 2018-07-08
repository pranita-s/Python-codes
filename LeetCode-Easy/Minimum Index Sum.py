# TIME - O(m + n)
# SPACE - O(m + n)

def minIndexSum(list1,list2):
  
  d1 = {res:i for i,res in enumerate(list1)}
  d2 = {res:i for i,res in enumerate(list2)}
  
  lookup = {res:(d1[res]+d2.get(res,float('inf'))) for res in d1}
  
  m = min(lookup.values())
  
  return [res for res in lookup if lookup[res] == m]
