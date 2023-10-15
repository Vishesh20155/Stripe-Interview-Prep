from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        p = 1
        ans = []
        for row in grid:
            for c in row:
                p *= c
                
        for row in grid:
            t = []
            for c in row:
                t.append((int(p/c))%12345)
            ans.append(t.copy())
            
        return ans
    
s = Solution()
print(s.findIndices([5,1,4,1], 2, 4))