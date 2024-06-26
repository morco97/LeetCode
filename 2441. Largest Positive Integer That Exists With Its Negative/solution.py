class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        check = set(nums)
        maximal = -1
        for num in nums:
            if num > maximal and -1 * num in check:
                maximal = num
        return maximal  
