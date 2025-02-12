import heapq

class Tweet:

    def __init__(self, priority, content):
        self.priority = priority
        self.content = content

    def __lt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"Tweet(priority={self.priority}, content={self.content})"
    

class Twitter:

    '''
        To view 10 most recent tweets, can store a 
        priority queue of last timestamped elements
        in a max_heap.

        Once going over 10, will pop out the old ones.
    '''

    def __init__(self):
        self.globalTweet = 0
        self.tweetMap = {}
        self.followerMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.globalTweet = self.globalTweet + 1
        self.tweetMap[userId].append((tweetId, self.globalTweet))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetHeap = []
        # Checking followers
        if userId in self.followerMap:
            followers = self.followerMap[userId]
            for follower in followers:
                if follower in self.tweetMap:
                    for tweetId, priority in self.tweetMap[follower]:
                        heapq.heappush(tweetHeap, Tweet(priority, tweetId)) # max-heap

        # Check my own tweets
        if userId in self.tweetMap:
            for tweetId, priority in self.tweetMap[userId]:
                heapq.heappush(tweetHeap, Tweet(priority, tweetId))                

        tweetContent = []
        for i in range(1, 10 + 1):
            if tweetHeap:
                tweet = heapq.heappop(tweetHeap)
                tweetContent.append(tweet.content)

        return tweetContent

    def follow(self, followerId: int, followeeId: int) -> None:
        # Can't follow myself, don't add
        if followerId != followeeId:
            self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.followerMap and followeeId in self.followerMap[followerId]:
                self.followerMap[followerId].remove(followeeId)
        
