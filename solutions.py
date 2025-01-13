class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      """
      80. Remove Duplicates from Sorted Array II. LeetCode Medium.
      """
      total = 2
      index = 2
      while index < len(nums):
          total += 1
          if nums[index] == nums[index-2]:
                  nums.pop(index)
                  index -= 1
                  total -= 1
          index += 1
    
      return total if len(nums) >= 2 else 1
        
    def findMaxK(self, nums: List[int]) -> int:
        """
        2441. Largest Positive Integer That Exists With Its Negative
        """
        check = set(nums)
        maximal = -1
        for num in nums:
            if num > maximal and -1 * num in check:
                maximal = num
        return maximal
