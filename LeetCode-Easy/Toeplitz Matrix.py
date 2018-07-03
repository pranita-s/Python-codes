# TIME - O(RC)


def toeplitzMatrix(grid):
  R,C = len(grid),len(grid[0])
  
  for i in range(R):
    for j in range(C):
      if i + 1 < R and j + 1 < C:
        if grid[i][j] != grid[i+1][j+1]:
          return False
  return True
