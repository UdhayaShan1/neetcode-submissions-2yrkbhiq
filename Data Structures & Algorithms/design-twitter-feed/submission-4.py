class Tmp:
    def __init__(self, id, post, time):
        self.id = id
        self.post = post
        self.time = time
    def __lt__(self, o):
        return self.time > o.time

class Tmp2:
    def __init__(self, id, post, time):
        self.id = id
        self.post = post
        self.time = time
    def __lt__(self, o):
        return self.time < o.time

class Twitter:

    def __init__(self):
        self.posts = {}
        self.time = 0
        self.friends = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append(Tmp(userId, tweetId, self.time))
        self.time += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        hmm = []
        r = self.posts.get(userId, [])[::-1]
        for i in range(min(10, len(r))):
            ref = r[i]
            heapq.heappush(hmm, Tmp2(ref.id, ref.post, ref.time))
        #print(self.friends, userId, self.posts)
        #print("@@")
        #print(userId)
        # for i in hmm:
        #     print(i.post)
        #print(self.friends.get(userId, []))
        for i in self.friends.get(userId, []):
            #print('##', i)
            posts = self.posts[i][::-1]
            for j in range(min(10, len(posts))):
                ref = posts[j]
                if len(hmm) < 10:
                    heapq.heappush(hmm, Tmp2(ref.id, ref.post, ref.time))
                    continue
                if ref.time > hmm[0].time:
                    heapq.heappop(hmm)
                    heapq.heappush(hmm, Tmp2(ref.id, ref.post, ref.time))
        res = []
        while hmm:
            res.append(heapq.heappop(hmm).post)
        
        return res[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.friends:
            self.friends[followerId] = {}
        self.friends[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(followerId, followeeId)
        if followerId == followeeId:
            return
        if followeeId in self.friends.get(followerId, {}):
            del self.friends[followerId][followeeId]
        
