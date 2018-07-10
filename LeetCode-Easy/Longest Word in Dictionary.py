# TIME - O(n), n = total number of length of all the words
# SPACE - O(t), t = number of nodes in trie


import collections
class TrieNode:
  
  def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.word = ''
    self.end = False

class Trie:
  
  def __init__(self):
    self.root = TrieNode()
  
  def insertWord(self,word):
    node = self.root
    for c in word:
      node = node.children[c]
    node.word = word
    node.end = True
  
  def bfs(self):
    q = collections.deque([self.root])
    res = ''
    while q:
      popped = q.popleft()
      for child in popped.children:
        if child.end:
          if len(res) < len(child.word) or res < child.word:
            res = child.word
    return res
 

if __name__ == "__main__":
  t = Trie()
  words =  ["w","wo","wor","worl", "world"]
  for w in words:
    t.insertWord(w)
  return t.bfs
        
