# TIME - O(n)
# SPACE - O(26) - O(1)


def taskScheduler(tasks,n):  
  d = {}
  maxx = 0
  for num in nums:
    d[num] = d.get(num,0) + 1
    maxx = max(d[num],maxx)
  
  time = (maxx-1) * n
  for k,v in d.iteritems():
    if v == maxx:
      time += 1
  return max(len(tasks),maxx)
