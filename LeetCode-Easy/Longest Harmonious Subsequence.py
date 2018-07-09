# TIME - O(n)
# SPACE - O(n)

def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num,0)
        l =0
        for key in d:
            if (key+1) in d:
                l = max(l,d[key]+d[key+1])
        return l
