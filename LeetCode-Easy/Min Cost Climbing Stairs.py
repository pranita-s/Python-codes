# TIME - O(n)
# SPACE - O(n)


def minCost(cost):
  dp = [0] * (len(cost)+2)
  dp[1] = cost[0]
  cost.append(0)
  
  for i in range(2,len(dp)):
    dp[i] = min(dp[i-1],dp[i-2]) + cost[i-1]
  
  return dp[-1]
    
