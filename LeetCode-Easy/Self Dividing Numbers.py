# Time:  O(n)

def selfDividingNumbers(left,right):
  ans = []
  for num in range(left,right+1):
    curr = num
    while True:
      temp = curr % 10
      if curr == 0:
        ans.append(num)
      if temp == 0 or num % temp != 0:
        break
      
      curr /= 10
  
  return ans
