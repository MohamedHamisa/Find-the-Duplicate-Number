class Solution:
    def findDuplicate(self, nums):
            s = set(nums)
            return int((sum(nums) - sum(s))/(len(nums) - len(s)))
