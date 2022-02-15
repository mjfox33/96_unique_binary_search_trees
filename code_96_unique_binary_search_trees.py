class Solution:
    def numTrees(self, n: int) -> int:
        if n < 0:
            return None
        if n < 2:
            return 1
        result = 0
        for i in range(n):
            result += self.numTrees(i) * self.numTrees(n-i-1)
        
        return result

