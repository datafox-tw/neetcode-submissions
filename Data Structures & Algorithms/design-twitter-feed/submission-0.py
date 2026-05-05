class Twitter:

    def __init__(self):
        self.time = 0
        # follow map描述一個人追蹤的人有哪些
        self.followMap = defaultdict(set)
        #tweet map描述一個人發了哪些貼文
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        #我在某個時刻發了一則貼文
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #拿到我的文章
        feed = self.tweetMap[userId][:] #單位是list
        for followeeId in self.followMap[userId]:
            # 把我追蹤的人的文章也拿過來
            feed.extend(self.tweetMap[followeeId])
        #這個sort最麻煩但是第一版本先用這個
        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]
    #我可以follow他人
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
    #這個也簡單就只是直接從set裡面拿出來東西而已，add的相對是discard
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)