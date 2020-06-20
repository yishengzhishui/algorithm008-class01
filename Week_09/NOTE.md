[不同路径 2 ](https://leetcode-cn.com/problems/unique-paths-ii/)
状态转移方程:
```python
if obstacleGrid[i][j] == 1:
    dp[i][j] = 0

else:
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
```