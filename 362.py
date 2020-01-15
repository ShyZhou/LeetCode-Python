# Design Hit Counter

# Design a hit counter which counts the number of hits received in the past 5 minutes.
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume
# that calls are being made to the system in chronological order (ie, the timestamp is
# monotonically increasing). You may assume that the earliest timestamp starts at 1.
# It is possible that several hits arrive roughly at the same time.

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

import collections

class HitCounter(object):
    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        while self.queue and timestamp - self.queue[0] > 300:
            self.queue.popleft()
        return len(queue)

# Follow up: What if the number of hits per second could be very large? Does your design scale?

class HitCounter(object):
    def __init__(self):
        self.timestamps = []
        self.hits = []

    def hit(self, timestamp):
        idx = timestamp % 300
        if self.timestamps[idx] != timestamp:
            self.timestamps[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp):
        hits = 0
        for i in range(300):
            if self.timestamps[i] - timestamp < 300:
                hits += self.hits[i]
        return hits
