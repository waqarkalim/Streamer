import time
import datetime

start_time = time.time()

time.sleep(5)

end_time = time.time()

time = end_time - start_time


day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
