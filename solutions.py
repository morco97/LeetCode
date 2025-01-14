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

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        165. Compare Version Numbers
        """
        v1, v2 = version1.split('.'), version2.split('.')
        
        def helper(self, v1: list[str], v2: list[str]) -> int:
            if not v1 and not v2:
                return 0
            
            if not v1 and v2:
                cur = int(v2.pop(0))
                if cur > 0:
                    return -1
            
            if v1 and not v2:
                cur = int(v1.pop(0))
                if cur > 0:
                    return 1
            
            if v1 and v2:
                cur1, cur2 = int(v1.pop(0)), int(v2.pop(0))
                if cur1 > cur2:
                    return 1
                if cur1 < cur2:
                    return -1
            
            return self.helper(v1, v2)
            
        return self.helper(v1, v2)

        def rotate(self, nums: List[int], k: int) -> None:
        """
        189. Rotate Array. LeetCode Medium.
        """
        if len(nums) > 1:
            k = k % len(nums)
            nums[:len(nums) - k], nums[len(nums) - k: len(nums)] = nums[len(nums) - k: len(nums)], nums[:len(nums) - k]


    def reversePrefix(self, word: str, ch: str) -> str:
        """
        2000. Reverse Prefix of Word
        """
        if word[0] == ch:
            return word
        temp = word[0]
        for i in range(1, len(word) - 1):
            if word[i] == ch:
                temp += word[i]
                return temp[::-1] + word[i + 1:]
            temp += word[i]
        if word[-1] == ch:
            return word[::-1]
        return word
        
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
