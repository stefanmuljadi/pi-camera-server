"""
Continuously capture images from a webcam and write to a Redis store.
Usage:
   python recorder.py [width] [height]
"""

import itertools
import os
import redis
from picamera2 import Picamera2
import io 

store = redis.Redis()
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (1024, 768)}))
picam2.start()

for count in itertools.count(1):
   data = io.BytesIO()
   picam2.capture_file(data, format='jpeg')
   image_bytes = data.getvalue()
   store.set('image', image_bytes)
   store.set('image_id', os.urandom(4))