import heapq
from typing import List

class Twitter:
    def __init__(self):
        # followerId -> set of followeeIds
        self.followMap = {}

        # userId -> list of (time, tweetId)
        self.tweetMap = {}

        # Increasing timestamp so newer tweets have larger time
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweetMap:
            self.tweetMap[userId] = []

        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # User should see their own tweets too
        followees = self.followMap.get(userId, set()).copy()
        followees.add(userId)

        # Add the latest tweet from each followee to heap
        for followeeId in followees:
            if followeeId in self.tweetMap:
                tweets = self.tweetMap[followeeId]
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]

                # Use negative time because heapq is a min heap
                # Store idx so we can later fetch this user's previous tweet
                heapq.heappush(maxHeap, (-time, tweetId, followeeId, idx - 1))

        # Get up to 10 most recent tweets
        while maxHeap and len(res) < 10:
            negTime, tweetId, followeeId, nextIdx = heapq.heappop(maxHeap)
            res.append(tweetId)

            # Push the next most recent tweet from the same user
            if nextIdx >= 0:
                time, nextTweetId = self.tweetMap[followeeId][nextIdx]
                heapq.heappush(maxHeap, (-time, nextTweetId, followeeId, nextIdx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            # discard avoids crash if followeeId is not present
            self.followMap[followerId].discard(followeeId)