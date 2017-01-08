#!/usr/bin/env python

import argparse
import sys
import time
import picamera

def main():
    parser = argparse.ArgumentParser(
             prog='tl-capture',
             description='Captures a sequence of images for creating timelapse photos')

    parser.add_argument('-i, --interval', type=int, dest='interval', metavar='I', 
                        required=True, help='Time in seconds between captures.')
    parser.add_argument('-f, --frames', type=int, dest='frames', metavar='F',
                        required=True, help='Number of frames to capture')
    parser.add_argument('-o, --output-dir', type=str, dest='output_dir', metavar='dir',
                        default='.', help='The directory in which to save the images')

    ns = parser.parse_args()
    capture_frames(ns.frames, ns.interval, ns.output_dir)


def capture_frames(frames, interval, output_dir):
    camera = picamera.PiCamera()
    camera.hflip = True     
    camera.vflip = True

    for frame in range(frames):
        __capture_frame(camera, frame, output_dir)
        time.sleep(interval)


def __capture_frame(camera, frame, output_dir):
    camera.start_preview()
    file_name = '%s/frame_%04d.jpg' % (output_dir, frame)
    camera.capture(file_name)
    print 'wrote frame %d to %s' % (frame, file_name)

if __name__ == "__main__":
    main()
