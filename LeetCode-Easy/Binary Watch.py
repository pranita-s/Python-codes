# TIME - O(1)
# SPACE - O(1)

def binaryWatch(num):
  def countOnes(n):
    cnt = 0
    while n:
      cnt += n&1
      n >>= 1
    return cnt
  
  res = []
  for h in range(12):
    for m in range(60):
      if countOnes(h) + countOnes(m) == num:
        res.append('%d:%02d'%(h,m))
  return res
