
# TIME - O(RC)
# SPACE - O(RC)


def maxAreaOfIsland(grid):
  def DFS(i,j):
    a = 1
    grid[i][j] = 9
    neighbors = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
    for n in neighbors:
      if 0 <= n[0] < R and 0 <= n[1] < C and grid[n[0]][n[1]]:
        a += DFS(n[0],n[1])
    
    return a
  if len(grid) == 0:
    return 0
  R,C = len(grid),len(grid[0])
  area = 0 
  
  for i in range(R):
    for j in range(C):
      if grid[i][j] == 1:
        ar = DFS(i,j)
        area = max(area,ar)
  
  return area
