# TIME - O((R-L)log(R-L))


def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def countOnes(n):
            c = 0
            while n:
                if n & 1:
                    c +=1
                n = n >> 1
            return c
        
        
        primes = [2,3,5,7,11,13,17,19,23]
        count = 0
        for num in range(L,R+1):
            c = countOnes(num)
            if c in primes:
                count += 1
        return count
