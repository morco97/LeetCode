class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        return self.helper(v1, v2)
    
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
