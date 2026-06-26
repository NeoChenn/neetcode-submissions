class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [ i for i in range(N + 1) ]
        size = [1] * (N + 1)

        def find(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur] 
            return cur

        def union(n1, n2):
            par1 = find(n1)
            par2 = find(n2)
            if par1 == par2:
                return [n1, n2]
            if size[par1] > size[par2]:
                size[par1] += size[par2]
                par[par2] = par1
            else:
                size[par2] += size[par1]
                par[par1] = par2
            return None

        for n1, n2 in edges:
            res = union(n1, n2)
            if res != None:
                return res
                
