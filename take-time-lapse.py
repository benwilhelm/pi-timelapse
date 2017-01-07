import sys
import time
import picamera

FPS_OUTPUT = 60.
OUT_SPEED = 2.
VID_LENGTH = 1.

CAPTURE_INTERVAL = 1 / (FPS_OUTPUT / OUT_SPEED)
NUMBER_OF_FRAMES = (int) (FPS_OUTPUT * VID_LENGTH)
print NUMBER_OF_FRAMES

camera = picamera.PiCamera()
camera.hflip = True     
camera.vflip = True

def capture_frame(camera, frame):
    #camera.start_preview()
    file_name = 'frame_%04d.jpg' % (frame)
    camera.capture(file_name, use_video_port=True)
    print 'captured frame %d' % (frame)

for frame in range(NUMBER_OF_FRAMES):
    capture_frame(camera, frame)
    # print CAPTURE_INTERVAL
    time.sleep(CAPTURE_INTERVAL)
