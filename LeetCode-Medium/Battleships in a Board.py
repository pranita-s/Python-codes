# TIME - O(m * n)
# SPACE - O(1)

def battleshipsInABoard(grid):
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      count += (grid[i][j] == 'X') and (i == 0 or grid[i-1][j] != 'X') and (j==0 or grid[i][j-1] != 'X')
  
  return count
