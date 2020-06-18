
class UnionFind(object):
    def __init__(self, nodes):
        self.parents = {}
        self.ranks = {}

        for node in nodes:
            self.parents[node] = node
            self.ranks[node] = 1

    def find(self, node):
        parent = self.parents[node]

        # 尾递归
        if parent != node:
            parent = self.find(parent)

        # 路径压缩
        self.parents[node] = parent
        return parent

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

        return

    def connected(self, node_a, node_b):
        return self.parents[node_a] == self.parents[node_b]


if __name__ == '__main__':
    nodes = ['剑魂', '红眼', '漫游', '元素', '魔道', '战法', '大枪', '散打', '弹药', '机械']
    union_find = UnionFind(nodes)
    union_find.union('剑魂', '红眼')
    union_find.union('漫游', '大枪')
    union_find.union('漫游', '弹药')
    union_find.union('漫游', '机械')
    union_find.union('元素', '魔道')
    union_find.union('元素', '战法')

    print(union_find.connected('大枪', '弹药'))  # True
    print(union_find.connected('剑魂', '战法'))  # False
    print(union_find.connected('魔道', '散打'))  # False
    print(union_find.connected('魔道', '战法'))  # True

