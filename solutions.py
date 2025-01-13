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

  
