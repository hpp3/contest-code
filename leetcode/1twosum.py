class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        need = {} 
        for i, num in enumerate(nums):
            if num in need:
                return need[num], i
            need[target-num] = i
        return (0,0)
