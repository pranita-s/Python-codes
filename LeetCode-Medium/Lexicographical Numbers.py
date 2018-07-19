
# RECURSIVE

def lexicographicalNumbers(n):  
  res = []
  def dfs(curr_num):
    res.append(curr_num)
    curr_num *= 10
    for i in range(10):
      if curr_num + i <= n:
        dfs(curr_num+i)
  
  for i in range(1,min(10, n+1)):
    dfs(i)
  
  return res
 
# ITERATIVE

def lexicalOrder(n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new /= 10
            ans.append(new)    
        return ans
