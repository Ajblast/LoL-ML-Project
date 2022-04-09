import time

class RateLimit:
    #Rate is how many requests can be done in the time frame (In Seconds)
    def __init__(self, rate : int, timeFrame : int, timeEpsilon : float, sleepTime : float):
        self.rate = rate
        self.timeFrame = timeFrame
        self.timeEpsilon = timeEpsilon
        self.sleepTime = sleepTime
        self.requests = 0
        self.startTime = time.perf_counter()

    # Wait for the rate limit to be valid
    def waitForRateLimit(self):
        # Reset the rate limit if the timeframe has passed since starting
        if (self._DeltaTime() >= self.timeFrame):
            self._reset()

        # Increase request count
        self.requests += 1

        # If the request count equals the rate, wait for the passedTime + timeEpsilon to reach the time frame
        if (self.requests == self.rate):
            while (self._DeltaTime() + self.timeEpsilon < self.timeFrame):
                print("Waiting on request timeframe limit. Requests {}/{} | TimeFrame {:.2f}/{:.2f}".format(self.requests, self.rate, self._DeltaTime(), self.timeFrame))
                time.sleep(self.sleepTime)

    def _reset(self):
        self.requests = 0
        self.startTime = time.perf_counter()

    def _DeltaTime(self):
        return time.perf_counter() - self.startTime
