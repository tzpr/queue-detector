import cv2
import numpy as np
#from matplotlib import pyplot as plt
import schedule
import time
import random

'''
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
'''

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter()

img_index = 0

while 1:
    ret, frame = cap.read()

    # to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show live stream
    cv2.imshow('gray', gray)

    # capture keys
    k = cv2.waitKey(0) # waits forever for key stroke

    if k == ord('q'): # q to exit
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('coffee_queue_{}.png'.format(img_index), gray)
        img_index += 1


cap.release()    
cv2.destroyAllWindows() # destroy all created windows


# # schedule scheduler
# # https://pypi.org/project/schedule/
# schedule.every(10).seconds.do(check_queue)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
