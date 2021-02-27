import redis
import schedule
import time
import random
import jetson.inference
import jetson.utils


# connect to redis
message_broker = redis.Redis(host='localhost', port=6060)

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")  # V4L2 webcam


def analyze_queue_picture():
    img = camera.Capture()
    detections = net.Detect(img)

    # https://realpython.com/python-string-formatting/
    print(f'DEBUG the detections: {detections}')
    return 'daadaa'


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
