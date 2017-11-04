import math
import collections

def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    for i,row in enumerate(partial_assignment):
            for j,c in enumerate(row):
                if c != 0:
                    for k in ((i,str(c)),(str(c),j),(i/region_size,j/region_size,str(c))):
                        print("k",k)

easy = [[2,9,0,0,0,0,0,7,0],
       [3,0,6,0,0,8,4,0,0],
       [8,0,0,0,4,0,0,0,2],
       [0,2,0,0,3,1,0,0,7],
       [0,0,0,0,8,0,0,0,0],
       [1,0,0,9,5,0,0,6,0],
       [7,0,0,0,9,0,0,0,1],
       [0,0,1,2,0,0,3,0,6],
       [0,3,0,0,0,0,0,5,7]]
ans = is_valid_sudoku_pythonic(easy)
print(ans)