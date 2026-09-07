class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        for post in self.posts[userId][-10:]: 
            heapq.heappush(heap, post)
        for followeeId in self.followers[userId]:
            for post in self.posts[followeeId][-10:]: 
                heapq.heappush(heap, post)
        for i in range(10):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)