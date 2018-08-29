# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)

class UF:
  
  def __init__(self,n):
    self.set = range(n)
    self.count = n
  
  def findSet(self,x):
    if x != self.set[x]:
      self.set[x] = self.findSet(self.set[x])
    return self.set[x]
  
  def UnionSet(self,x,y):
    x_root,y_root = self.findSet(x), self.findSet(y)
    if x_root != y_root:
      self.set[min(x_root,y_root)] = max(x_root,y_root)
      self.count -= 1


class Solution:
  
  def findConnectedComponents(self,n,edges):
    uf = UF(n)
    for u,v in edges:
      uf.UnionSet(u,v)
    return uf.count
