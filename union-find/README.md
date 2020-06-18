# 并查集

## 基本概念
并查集也被称为不相交集数据结构（Disjoint Set）。顾名思义，并查集主要操作是合并与查询，它是把初始不相交的集合经过多次合并操作后合并为一个大集合，然后可以通过查询判断两个元素是否已经在同一个集合中了。

并查集的应用场景一般就是动态连通性的判断，例如判断网络中的两台电脑是否连通，在程序中判断两个变量名是否指向同一内存地址等。

## 思路
使用一个dict来存储并查集，其中dict的key, value分别是并查集中的一个节点及其父节点，并随着节点之间的连接关系动态变化。

## API
```python
class UnionFind(object):
    def __init__(self, nodes):
        # 根据传入的nodes初始化长度为len(nodes)的并查集
        return
    
    def find(self, node):
        # 找出node的父节点
        return
    
    def union(self, node_a, node_b):
        # 合并node_a和node_b所在的两个集合
        return 

    def connected(self, node_a, node_b):
        # 判定node_a和node_b是否在同一集合
        return 
```

## 方法
* 初始化  
字典 self.parents 存储每个节点的父节点，初始化时为该节点本身
字典 self.ranks 存储每个节点所在集合的规模，初始化为1
```python
    def __init__(self, nodes):
        self.parents = {}
        self.ranks = {}

        for node in nodes:
            self.parents[node] = node
            self.ranks[node] = 1
```
* 查找节点的父节点
使用尾递归不断查找父节点，同时使用路径压缩避免级联。
```python
    def find(self, node):
        parent = self.parents[node]

        # 尾递归
        if parent != node:
            parent = self.find(parent)

        # 路径压缩
        self.parents[node] = parent
        return parent
```

* 两个节点集合合并
根据节点所在的规模rank值确定合并方向
```python
    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)

        if parent_a != parent_b:
            rank_a = self.ranks[parent_a]
            rank_b = self.ranks[parent_b]

            if rank_a < rank_b:
                self.parents[parent_a] = parent_b
                self.ranks[parent_b] = rank_a + rank_b

                self.ranks.pop(parent_a)
            else:
                self.parents[parent_b] = parent_a
                self.ranks[parent_a] = rank_a + rank_b

                self.ranks.pop(parent_b)
```

* 判定两个节点是否联通
```python
    def connected(self, node_a, node_b):
        return self.parents[node_a] == self.parents[node_b]
```
