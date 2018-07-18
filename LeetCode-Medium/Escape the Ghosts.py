# TIME - O(n)

def escape(ghosts,target):
  
  diff = abs(target[0]) + abs(target[1])
  
  return all(diff < abs(target[0]-i)+abs(target[1]-j) for i,j in ghosts)
