class Tmp:
    def __init__(self, p, time):
        self.p = p
        self.time = time
    def __lt__(self, o):
        return self.time > o.time

class Twitter:

    def __init__(self):
        self.time = 0
        self.userPost = {}
        self.follow_map = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userPost:
            self.userPost[userId] = []
        self.userPost[userId].append((tweetId, self.time))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        users = [userId]
        for i in self.follow_map.get(userId, {}):
            users.append(i)
        #print(users)
        for i in users:
            postList = self.userPost.get(i, [])[::-1]
            for j in range(min(10, len(postList))):
                heapq.heappush(pq, Tmp(postList[j][0], postList[j][1]))
        res = []
        for i in range(10):
            if not pq:
                break
            res.append(heapq.heappop(pq).p)
        #print(res)
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = {}
        if followerId != followeeId:
            self.follow_map[followerId][followeeId] = 1

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map and followeeId in self.follow_map[followerId]:
            del self.follow_map[followerId][followeeId]

        
