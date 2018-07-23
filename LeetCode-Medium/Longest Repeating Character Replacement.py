# TIME - O(n)

def longestRepeating(s,k):
  import collections
  maxx = 0
  left= 0
  d = collections.defaultdict(int)
  for right, c in enumerate(s):
    d[c] += 1
    if left < right and (right - left + 1) - max(d.values()) > k:
      d[s[left]] -= 1
      left += 1
    maxx = max(maxx,(right-left+1))
  
  return maxx
  
