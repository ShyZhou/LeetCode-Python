# Moving Average from Data Stream

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

class MovingAverage(object):
    def __int__(self, window_size):
        self._size = window_size
        self._sum = 0
        self._q = collections.deque()

    def next(self, val):
        if len(self._q) == self._size:
            self._sum -= self._q.popleft()
        self._sum += val
        self._q.append(val)
        return self._sum / len(self._q)
