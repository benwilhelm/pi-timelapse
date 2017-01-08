#!/bin/bash

dir=.
rate=60

while getopts "d:r:" opt; do
  case $opt in
    d)
      echo "dir=$OPTARG"
      dir=$OPTARG
      ;;
    r)
      echo "rate=$OPTARG"
      rate=$OPTARG
      ;;
  esac
done

ffmpeg -y -f image2    \
-framerate $rate       \
-i $dir/frame_%04d.jpg \
-r $rate               \
-vcodec libx264        \
-profile high          \
-preset slow           \
$dir/timelapse.mp4
