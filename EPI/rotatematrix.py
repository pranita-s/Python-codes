# class RotatedMatrix:
#
#     def __init__(self,mat):
#         self._mat = mat
#
#     def read_entry(self,i,j):
#         return self._mat[~j][i]
#
#     def write_entry(self,i,j,v):
#         self._mat[~j][i] = v

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in range(4):
    for j in range(4):
        print(mat[~j][i])