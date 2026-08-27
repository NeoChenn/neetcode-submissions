class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        two accounts belong to the same person if there is some common email to both accounts
        create adjList for each email (email, name) : [emails]
        use DFS and visited set to find all connected emails, and add it to res
        repeat process until no unvisited emails remaining
        """
        adjList = {}
        for account in accounts:
            if len(account) == 2:
                adjList[account[1]] = [account[0]]
            else:
                for i in range(2, len(account)):
                    if account[i - 1] not in adjList:
                        adjList[account[i - 1]] = [account[0]]
                    if account[i] not in adjList:
                        adjList[account[i]] = [account[0]]
                    adjList[account[i - 1]].append(account[i])
                    adjList[account[i]].append(account[i - 1])
        
        res = []
        connected = []
        visited = set()

        def connectedEmails(email):
            if email in visited:
                return
            connected.append(email)
            visited.add(email)
            for i in range(1, len(adjList[email])):
                connectedEmails(adjList[email][i])
            

        for email in adjList.keys():
            if email in visited:
                continue
            connectedEmails(email)
            connected.sort()
            res.append([adjList[email][0]] + connected)
            connected = []
        
        return res
            
        