# TIME - O(n) n is total sum of length of words:
# SPACE - O(t) total number of nodes in trie


class Solution:

  def __init__(self):
    self.root = {}
  
  def levelOrderTraversal(self):
    q = [self.root]
    level = 0
    ans = 0
    while q:
      q0 = []
      level += 1
      for node in q:
        if not node:
          ans += level
        else:
          q0 += list(node.values())
      q = q0      
   return ans

  def insertWord(self,word):
    node = self.root
    for c in word:
      if c not in node:
        node[c] = {}
      node = node[c]
     
  def minimumLengthEncoding(self,words):
   
    for word in words:
      w = word[::-1]
      self.insertWord(w)

    return self.levelOrderTraversal()
