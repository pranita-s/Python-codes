# TIME - O(mn)


def islandPerimeter(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid = [[1]]:
            return 4
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count_of_ones = 0
                neighbors = [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]
                for n in neighbors:
                    if 0 <= n[0] < len(grid) and 0<= n[1] < len(grid[0]) and grid[i][j]==1:
                        if grid[n[0]][n[1]] == 1:
                            count_of_ones += 1
                if count_of_ones == 2:
                    perimeter += 2
                elif count_of_ones == 1:
                    perimeter += 3
        return perimeter
