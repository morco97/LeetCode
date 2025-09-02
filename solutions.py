class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters. LeetCode meduim.
        """
        visited = {}
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] not in visited:
                longest = max(r - l + 1, longest)
            else:
                if visited[s[r]] < l:
                    longest = max(longest, r - l + 1)
                else:
                    l = visited[s[r]] + 1
            visited[s[r]] = r
        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters. LeetCode meduim.
        Sliding window solution.
        """
        l, r = 0, 0
        maxSize = 0
        seen = set()
        while r < len(s):
            if (s[r] in seen):
                seen.remove(s[l])
                l += 1
            else:
                maxSize = max(maxSize, r - l + 1)
                seen.add(s[r])
                r += 1
        return maxSize


    def longestPalindrome(self, s: str) -> str:
        """
        5. Longest Palindromic Substring. LeetCode medium.
        """
        longest = ""
        lenLongest = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lenLongest:
                    longest = s[l:r + 1]
                    lenLongest = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lenLongest:
                    longest = s[l:r + 1]
                    lenLongest = r - l + 1
                l -= 1
                r += 1
        return longest

    def convert(self, s: str, numRows: int) -> str:
        """
        6. Zigzag Conversion. LeetCode medium.
        """
        if numRows == 1 or numRows >= len(s):
            return s

        container = ["" for _ in range(numRows)] 
        goingDown = False
        row = 0
        for ch in s:
            container[row] += ch
            if row == 0 or row == numRows - 1:
                goingDown = not goingDown
            row += 1 if goingDown else -1
        return "".join(container)

    def reverse(self, x: int) -> int:
        """
        7. Reverse Integer. LeetCode meduim.
        """
        ans = list(str(x))
        prefix = ans[0] if ans[0] == "-" else ""
        if not prefix:
            ans = ans[::-1]
            ans = "".join(ans)
        else:
            ans = ans[1:]
            ans = ans[::-1]
            ans = "".join(ans)
            ans = prefix + ans
        return int(ans) if int(ans) >= (-2) ** 31 and int(ans) <= ((2 ** 31) -1 ) else 0

    def myAtoi(self, s: str) -> int:
        """
        8. String to Integer (atoi). LeetCode medium.
        """
        def round(res):
            if res < -2 ** 31:
                return -2 ** 31
            if res > ((2 ** 31) - 1):
                return (2 ** 31) - 1
            return res

        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        lead = True
        res = 0
        neg = False
        for ch in s:
            if lead:
                if ch == " ":
                    continue
                elif ch == "0":
                    lead = False 
                    continue
                elif ch == "-" or ch == "+":
                    neg = True if ch == "-" else False
                    lead = False
                elif ch in digits and ch !="0":
                    res *= 10
                    res += int(ch)
                    lead = False
                else:
                    break
            elif ch in digits:
                res *= 10
                res += int(ch)
            else:
                break
        res = (-1) * res if neg else res
        return round(res)

    def maxArea(self, height: List[int]) -> int:
        """
        11. Container With Most Water. LeetCode meduim.
        """
        r, l = 0, len(height) - 1
        maximal = (l - r) * min(height[r], height[l])
        while r < l:
            if height[r] < height[l]:
                r += 1
            else:
                l -= 1
            temp = (l - r) * min(height[r], height[l])
            maximal = max(maximal, temp)
        return maximal

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        15. 3Sum. LeetCode meduim.
        """
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[r] + nums[l]

                if total == 0:
                    ans.append([nums[i], nums[r], nums[l]])
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    r -= 1
                    l += 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        36. Valid Sudoku. LeetCode meduim
        """
        for i in range(len(board)):
            appeared_row = set()
            appeared_col = set()
            for j in range(len(board)):
                if board[i][j].isdigit():      
                    if board[i][j] in appeared_row:
                        return False
                    appeared_row.add(board[i][j])
                if board[j][i].isdigit():    
                    if board[j][i] in appeared_col:
                        return False
                    appeared_col.add(board[j][i])
        boxes = [(0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6)]
        for box in boxes:
            appeared = set()
            for i in range(3):
                for j in range(3):
                    if board[i+box[0]][j+box[1]].isdigit():    
                        if board[i+box[0]][j+box[1]] in appeared:
                            return False
                        appeared.add(board[i+box[0]][j+box[1]])
        return True
            
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

    def maxProfit(self, prices: List[int]) -> int:
        """
        122. Best Time to Buy and Sell Stock II. LeetCode medium.
        """
        total, maximal, l, r = 0, 0, 0, 1
        while r < len(prices):
            if prices[r] - prices[l] < maximal:
                l += 1
                r += 1
            else:
                total += prices[r] - prices[l] 
                l = r
                r += 1
                maximal = 0
        return total

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

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        167. Two Sum II - Input Array Is Sorted. LeetCode medium.
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[r] + numbers[l]
            if total == target:
                return[l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        189. Rotate Array. LeetCode Medium.
        """
        if len(nums) > 1:
            k = k % len(nums)
            nums[:len(nums) - k], nums[len(nums) - k: len(nums)] = nums[len(nums) - k: len(nums)], nums[:len(nums) - k]

    def compress(self, chars: List[str]) -> int:
        """
        443. String Compression. LeetCode meduim.
        """
        i = 0
        index = 0
        while i < len(chars):
            char = chars[i]
            counter = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                counter += 1
            chars[index] = char
            index += 1
            if counter > 1:
                for ch in str(counter):
                    chars[index] = ch
                    index += 1
        return index


    def countSubstrings(self, s: str) -> int:
        """
        647. Palindromic Substrings. LeetCode meduim.
        """
        counter = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
        return counter

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """994. Rotting Oranges. LeetCode Meduim. BFS """
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append([r, c, 0])
        if not fresh: return 0

        while rotten and fresh:
            r, c, time = rotten.popleft()
            for i,j in [[r+1, c], [r-1, c], [r,c+1], [r,c-1]]:
                if i>=0 and i<rows and j>=0 and j<cols and grid[i][j] == 1:
                    fresh -= 1
                    if fresh == 0:
                        return time + 1
                    grid[i][j] = 2
                    rotten.append([i, j, time + 1])
        return -1

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """1926. Nearest Exit from Entrance in Maze. LeetCode Meduim, BFS"""
        rows, cols = len(maze), len(maze[0])
        cells = [(entrance[0], entrance[1], 0)]
        maze[entrance[0]][entrance[1]] = '+'

        while cells:
            row, col, steps = cells.pop(0)
            
            for i,j in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
                if i>=0 and j>=0 and i<rows and j<cols and maze[i][j] == '.':
                    cells.append((i, j, steps + 1))
                    if i==0 or j==0 or i==rows-1 or j==cols-1 and maze[i][j]=='.':
                        return steps + 1 
                    maze[i][j] = '+'
        
        return -1

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
