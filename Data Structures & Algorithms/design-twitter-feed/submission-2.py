class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        fetches 10 most recent tweet IDs
        posted by users who the user is following or by the user themself

        to keep track of who a user follows
            userId : set(followingIds)

        to keep track of a user's posts
            userId : [[postTime, tweetId]...]

        for each followingIds and themselves, take their 10 most recent tweets and add to heap:
            either going through each user and using heapify O(n^2)
            or heappush directly (nlogn)
        """
        res = []
        heap = []
        for post in self.posts[userId][-10:]: 
            heapq.heappush_max(heap, post)
        for followeeId in self.followers[userId]:
            for post in self.posts[followeeId][-10:]: 
                heapq.heappush_max(heap, post)
        for _ in range(10):
            if not heap:
                break
            res.append(heapq.heappop_max(heap)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
