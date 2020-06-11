# 动态规划 Dynamic Programming 

1、本质上与递归相同，将复杂问题拆解为简单的子问题；

2、Divide & Conquer + Optimal substructure 分治+最优子结构

动态规划 和 递归或者分治 没有根本上的区别
## 三步法

1. 划分子问题
2. **确定状态定义方法**（重点难点）
3. 推导状态转移方程(dp方程)，注意边界情况处理

## 注意
1. 人肉递归低效、很累
2. 找到最近最简方法，将其拆解成可重复解决的问题 
3. 数学归纳法思维(抵制人肉递归的诱惑)

### 买卖股票

#### 穷举框架

穷举出所有可能的状态，根据状态进行对应的操作更新状态：

```python
for 状态1 in 状态1的所有值：
		for 状态2 in 状态2的所有值：
  			for .....:
      			dp[状态1][状态2][...] = 选择
```

买卖股票中

`dp[i][k][0,1]`:**k是已经交易的次数**，i是天数，{0， 1}未持有，持有。

基本的全部组合就是：

```python
for i in range(n):
	for k in range(K, 0, -1):
    for s in [0, 1]:
      dp[i][k][s] = max(buy, sell, rest)
      
 return dp[-1][K][0]
```

 所以DP状态方程：

```python
dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
```

the base case:

```shell
dp[i][0][1] 没有交易下是不可能持有股票的，不存在
dp[i][0][0] = 0
```





