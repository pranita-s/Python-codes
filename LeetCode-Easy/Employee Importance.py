# TIME - O(n)
# SPACE - O(h)

def employeeImportance(employees,id):
  
  if employees[id-1] is None:
    return 0
  result = employees[id-1].importance
  for idx in employees[id-1].subordinates:
    result += employeeImportance(employees,idx)
  return result
  

# TIME - O(n)
# SPACE - O(w)

import collections
def employeeImportance(employees,id)
  q = collections.deque([id])
  result = 0
  while q:
    curr = q.popleft()
    result += employees[curr-1].importance
    for idx in employees[curr-1].subordinates:
      q.append(idx)
  return result
  
