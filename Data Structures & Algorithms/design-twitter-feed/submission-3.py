class Twitter:

    def __init__(self):
        self.time = 0 # increasing time stamp
        self.tweets = defaultdict(list) # users own tweets (timestamp, tweetid)
        self.following = defaultdict(set) # set of users they follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxH = []

        users = self.following[userId] | {userId}
        for uid in users: # fetching tweets from users
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetid = self.tweets[uid][index]

                heapq.heappush(maxH, (-time, tweetid, uid, index-1))
        
        # Merge the tweet streams, taking at most 10 newest tweets.
        while maxH and len(res) < 10:
            negTime, tweetid, uid, nextidx = heapq.heappop(maxH)
            res.append(tweetid)
            if nextidx >= 0:
                time, tweetid = self.tweets[uid][nextidx]
                heapq.heappush(maxH, (-time, tweetid, uid, nextidx-1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
