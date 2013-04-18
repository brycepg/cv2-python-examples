#!/usr/bin/env python

"""
This example shows how to retrive a VideoCapture object from a video file/device and 
then display it onto a window

Supply the argument 
    'h' to view the http video file
    'l' to view the local video file
    'u' to use a usb camera device(not included)

Examples:
    python video-capture-example.py h
    python video-capture-example.py l
    python video-capture-example.py u

"""

import cv2
import sys

# The video file mjpg/video.mjpg is simply being accessed on a http server
# (this is a live feed)
http_video_file = "http://myapplecam.com/mjpg/video.mjpg"

# This is a locally saved file
local_video_file = "drop.avi"

# This will select the first initilized camera device -- 
#   either a integrated webcam or a usb device
cameraDevice = 0

default_video = http_video_file

def print_usage():
    print """Usage: python video-capture-example.py [h|l|u]
    h: http video file
    l: local video file
    u: usb or integrated camera device"""

if __name__ == '__main__':

    argument_length = len(sys.argv)
    if argument_length == 1:
        # no supplied argument is okay -- use default
        video_file_type = ""
    elif argument_length == 2:
        # if there is a supplied argument, make sure there is only one
        video_file_type = sys.argv[1]
    else:
        # otherwise print an error 
        print_usage()
        exit(1)
        


    # Note: in cv2 the VideoCapture function can be used to create feeds from 
    #   both a usb device or a file 

    capture = ""
    if video_file_type == 'h':
        capture = http_video_file
    elif video_file_type == 'l': 
        capture = local_video_file
    elif video_file_type == 'u': 
        capture = cameraDevice
    elif video_file_type == "":
        # no supplied 
        capture = default_video
    else:
        print_usage()
        exit(1)

    # http://askville.amazon.com/open-avi-file-opencv/AnswerViewer.do?requestId=60162829
    video_capture = cv2.VideoCapture(capture)

    while True:

        # The video capture object can then be used to read frame by frame
        #   The img is literaly an image
        # is_sucessfuly_read is a boolean which returns true or false depending
        #   on weather the next frame is sucessfully grabbed.
        is_sucessfully_read, img = video_capture.read()

        # is_sucessfuly_read will return false when the drop.avi file ends
        if(is_sucessfully_read):
            cv2.imshow("Camera Feed", img)
        else:
            print "Cannot read video capture object from %s. Quitting..." % capture
            break

        # The waitKey function is odd because it has two functions.
        # First, it delays the loop for a specified amount of miliseconds as to 
        #   limit the frames per second and cpu usage
        # Second, it allows OpenCV to process events, including creating
        #   a window and redrawing the image every loop.
        # Basically it's required.
        cv2.waitKey(30)
