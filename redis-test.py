import redis
import schedule
import time
import random


# connect to redis
# https://redis.io/topics/quickstart
# https://github.com/andymccurdy/redis-py
message_broker = redis.StrictRedis(host='localhost', port=6379, db=0)


def analyze_queue_picture():
    # just some fake values
    if (random.randint(0, 10)) % 2 == 0:
        return 'queue'
    else:
        return 'no-queue'


def check_queue():
    queue_state = analyze_queue_picture()
    print('Current queue state: ', queue_state)

    if message_broker.get('queue_state') is not queue_state:
        message_broker.set('queue_state', queue_state)


# schedule scheduler
# https://pypi.org/project/schedule/
schedule.every(10).seconds.do(check_queue)

while True:
    schedule.run_pending()
    time.sleep(1)