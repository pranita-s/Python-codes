# TIME - O(n)

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import random
        while True:
            r = random.choice(nums)
            if nums.count(r) > len(nums)/2:
                return r
           
           

def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]
