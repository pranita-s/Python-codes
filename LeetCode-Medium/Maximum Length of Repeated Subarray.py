# TIME - O(MN)
# SPACE - O(min(M,N))


def maxSubarray(A,B):
  
  if len(A) < len(B):
    return maxSubarray(B,A)
  
  dp = [[0 for _ in range(len(B)+1)] for _ in range(2)]
  
  result = 0
  
  for i in range(len(A)):
    for j in range(len(B)):
      if A[i] = B[j]:
        dp[i%2][j+1] = 1 + dp[(i+1)%2][j]
      else:
        dp[i%2][j+1] = 0
    result = max(result,max(dp[i%2]))
  
  return result
  
