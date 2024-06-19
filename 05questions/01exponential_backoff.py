# exponential backoff
'''
that doubles the wait time b/w the retries starting
from 1 second, but stop after 5 retries
'''

import time


waitTime = 1
maxRetries = 5
attempts = 0

while attempts < maxRetries:
    print("attempt: ", attempts + 1 , "-- wait time", waitTime)
    time.sleep(waitTime)
    waitTime *= 2
    # waitTime = waitTime * 2
    attempts +=1