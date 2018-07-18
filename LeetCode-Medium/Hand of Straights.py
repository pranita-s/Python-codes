# TIME - O(nlogn)
# SPACE - O(n)

import collections
def handOfStraights(hand,W):
  lookup = collections.Counter(hand)
  for card in sorted(lookup):
    if lookup[card] > 0:
      for j in range(W)[::-1]:
        lookup[card+j] -= lookup[card]
        if lookup[card+j] < 0:
          return False
 return True
  
