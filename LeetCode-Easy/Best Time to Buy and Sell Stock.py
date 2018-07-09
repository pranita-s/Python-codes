# TIME - O(n)

def maxProfit(prices):
  minSoFar = prices[0]
  maxProfit = 0
  for price in prices[1:]:
    if price > minSoFar:
      maxProfit = max(maxProfit,price-minSoFar)
    minSoFar = min(minSoFar, price)
  
  return maxProfit
