import math
import time
import progressbar


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
            widgets = ["Waiting RateLimit [", progressbar.Counter(format='%(value)02d/%(max_value)d'), '][', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']']
            
            bar = progressbar.ProgressBar(max_value=math.trunc(self.timeFrame + self.timeEpsilon))
            bar.update(math.trunc(self._DeltaTime()))
            while (self._DeltaTime() < self.timeFrame + self.timeEpsilon):
                bar.update(math.trunc(self._DeltaTime()))
                time.sleep(self.sleepTime)

    def _reset(self):
        self.requests = 0
        self.startTime = time.perf_counter()

    def _DeltaTime(self):
        return time.perf_counter() - self.startTime
