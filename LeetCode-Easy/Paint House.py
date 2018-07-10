#There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs0 is the cost of painting house 0 with color red; costs1 is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
#Note: All costs are positive integers.


# TIME - O(n)


def paintHouse(costs):
  n = len(costs)
  
  for i in range(1,n):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][2], costs[i-1][0])
    costs[i][2] += min(costs[i-1][1], costs[i-1][0])
  
  return min(costs[n-1])
