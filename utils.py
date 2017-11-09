import time
import math

def time_since(since):

    def _as_minutes(s):
        m = math.floor(s / 60)
        s -= m * 60
        return '%dm %ds' % (m, s)

    now = time.time()
    s = now - since

    return '%s' % (_as_minutes(s))