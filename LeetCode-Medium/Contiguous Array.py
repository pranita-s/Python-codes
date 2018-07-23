# TIME - O(n)
# SPACE - O(1)

def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {0:0}
        
        res = 0
        cnt = 0
        for i, num in enumerate(nums,1):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt in d:
                res = max(res,i - d[cnt])
            else:
                d[cnt] = i
        return res
