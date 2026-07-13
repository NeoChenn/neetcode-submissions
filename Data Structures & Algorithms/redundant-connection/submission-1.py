class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            if rank[node1] >= rank[node2]:
                parents[p2] = p1
                tmp = rank[p2]
                rank[p2] = 1
                rank[p1] += tmp
            else:
                parents[p1] = p2
                tmp = rank[p1]
                rank[p1] = 1
                rank[p2] += tmp
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
