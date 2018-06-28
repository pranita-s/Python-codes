def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        num_candies = len(candies)/2
        unique = set(candies)
        num_unique = len(unique)
        
        return min(num_candies,num_unique)
