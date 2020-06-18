## 字典树 Trie

### 字典树数据结构

- 字典树，即 Trie 树，又称单词查找树或键树，是一种树形结构。典型应用于统计和排序大量的字符串（但不仅限于字符串）所以经常被搜索引擎系统用于文本词频统计。
- 优点：最大限度的减少无谓的字符串比较，查询效率比hash表高

### 字典树核心思想

- 空间换时间
- 利用字符串公共前缀降低查询时间开销，以达到提高效率目的

### 字典树的基本性质

- 节点本身不存完整单词
- 从根结点到某一结点，路径上经过的结点连接起来，为该结点对应的字符串
- 每个结点的所有子结点路径代表的字符都不相同

### trie 树模板

```python
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

## 并查集

### 适用场景

- 组团配对问题
- Group or not？

### 基本操作

- makeSet(s) : 建立一个新的并查集，其中包含s个单元素集合
- unionSet(x, y): 把 x 和 y 所在的集合合并，要求 x 和 y 所在的集合不想交，如果相交则不合并。
- find(x) : 找到x所在集合的代表，该操作也可用于判断两个元素是否在同一个集合，只要将他们各自代表比较下就可以了。

### 代码模板

``` python
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```

## 红黑树

Red-black Tree

红黑树是一种近似平衡的二叉搜索树(Binary Search Tree)，它能够确保任何一个结点的左右子树的高度差小于两倍。具体来说，红黑树是满足如下条件的二叉搜索树：

- 每个结点要么是红色，要么是黑色。
- 根节点是黑色。
- 每个叶节点(NIL节点，空节点)是黑色的。
- 不能有相邻接的两个红色节点。
- 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。

### 关键性质

从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

## AVL树

1. Balance Factor(平衡因子)：是它的左子树的高度减去它的右子树的高度(有时相反)。balance factor = {-1, 0, 1}
2. 通过旋转操作来进行平衡(四种)

### 记录左右子树高度

### 旋转操作

1. 左旋

   **子树形态:右右子树 —> 左旋**

2. 右旋

   **子树形态:左左子树 —> 右旋**

3. 左右旋

   **子树形态:左右子树 —> 左右旋**

4. 右左旋

   **子树形态:右左子树 —> 右左旋**

## AVL树总结

1. 平衡二叉搜索树
2. 每个结点存 balance factor = {-1, 0, 1}
3. 四种旋转操作
4. 不足：结点需要存储额外信息、且调整次数频繁