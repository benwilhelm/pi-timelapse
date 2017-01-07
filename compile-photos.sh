#!/bin/bash

ffmpeg -y -f image2 -i ./frame_%04d.jpg -r 60 -vcodec libx264 -profile high -preset slow ./timelapse.mp4
