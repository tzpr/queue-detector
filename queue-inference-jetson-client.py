import redis
import schedule
import time
import random
import jetson.inference
import jetson.utils


# connect to redis
message_broker = redis.Redis(host='localhost', port=6060)

net = jetson.inference.detectNet('ssd-mobilenet-v2', threshold=0.5)
camera = jetson.utils.videoSource('/dev/video0')  # V4L2 webcam


def analyze_queue_picture():
    number_of_persons = 0
    PERSON_CLASS_ID = 1
    queue_state = 'no queue'

    img = camera.Capture()
    detections = net.Detect(img)

    for idx in detections:
        if detections[idx].ClassID == PERSON_CLASS_ID:
            number_of_persons = number_of_persons + 1

    # https://realpython.com/python-string-formatting/
    print(f'DEBUG number of persons: {number_of_persons}')

    if number_of_persons > 1:
        queue_state = 'queue'

    return queue_state


def check_queue():
    queue_state = analyze_queue_picture()
    print('Current queue state: ', queue_state)

    if message_broker.get('queue_state') is not queue_state:
        message_broker.set('queue_state', queue_state)


# schedule scheduler
# https://pypi.org/project/schedule/
schedule.every(5).seconds.do(check_queue)

while True:
    schedule.run_pending()
    time.sleep(1)
