# TIME - O(n**2)
# SPACE - O(n**2)

import heapq

def risingWater(grid):
  n = len(grid)
  q = []
  maxH = 0
  directions = [[-1,0],[0,-1],[1,0],[0,1]]
  heapq.heappush((grid[0][0],(0,0)))
  while True:
    ht, (x,y) = heapq.heappop(q)
    maxH = max(maxH,ht)
    if x == n-1 and y == n-1:
      return maxH
    for d in directions:
      xx = x + d[0]
      yy = y + d[1]
      if 0<= xx < n and 0<= y <n and grid[xx][yy] >=0:
        heapqheappush(q,(grid[xx][yy],(xx,yy)))
      
    
