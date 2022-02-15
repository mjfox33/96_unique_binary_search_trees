class Solution:
    def numTrees(self, n: int) -> int:
        if n < 0:
            return None
        if n < 2:
            return 1
        result = [0]*(n+1)
        result[0] = 1
        result[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                result[i] +=  result[j] * result[i-j-1]
        return result[n]