# TIME - O(n)
# SPACE - O(n)


def containsDuplicate(nums):
  return len(nums) > len(set(nums))
