#!/usr/bin/env
'''
emulate a chameleon camera, getting images from a playback tool

The API is the same as the chameleon module, but takes images from fake_chameleon.pgm
'''

from . import chameleon
import time, os, glob, sys, cv, numpy

from cuav.lib import cuav_util
from cuav.image import scanner

error = chameleon.error
continuous_mode = False
fake = 'fake_chameleon.jpg'
frame_counter = 0
trigger_time = 0
frame_rate = 7.5
chameleon_gamma = 950
last_frame_time = 0

def open(colour, depth, brightness):
    return 0

def trigger(h, continuous):
    global continuous_mode, trigger_time
    continuous_mode = continuous
    trigger_time = time.time()


def load_image(filename):
    if filename.endswith('.pgm'):
        fake_img = cuav_util.PGM(filename)
        return fake_img.array
    img = cv.LoadImage(filename)
    array = numpy.asarray(cv.GetMat(img))
    grey = numpy.zeros((1200,1600), dtype='uint8')
    scanner.rebayer(array, grey)
    return grey
    

def capture(h, timeout, img):
    global continuous_mode, trigger_time, frame_rate, frame_counter, fake, last_frame_time
    tnow = time.time()
    due = trigger_time + (1.0/frame_rate)
    if tnow < due:
        time.sleep(due - tnow)
        timeout -= int(due*1000)
    # wait for a new image to appear
    basepath = os.path.expanduser("~/temp_image_folder/")
    while True:
        try:
            list_of_files = glob.glob(basepath+'*')
            if not list_of_files:
                raise chameleon.error("No image available in specified folder")
                frame_time = 0
                break
            # latest_file = max(list_of_files,key=os.path.getctime)
            # filename = latest_file
            files = sorted(list_of_files, key=os.path.getctime, reverse=True)
            filename = files[1]
            # print('Got filename ' + filename)
            frame_time = cuav_util.parse_frame_time(filename)
            # print "Got frame time %f" % frame_time
            break
        except Exception:
            raise chameleon.error("Unexpected file search error")
            frame_time = 0
            break
            pass
    # frame_time = time.mktime(time.gmtime())
    # print('Got base frame time %g' % frame_time)

    # If no new image is available
    while (frame_time == last_frame_time or frame_time == 0) and timeout > 0:
        timeout -= 10
        time.sleep(0.01)
        try:
            list_of_files = glob.glob(basepath+'*')
            if not list_of_files:
                raise chameleon.error("No image available in specified folder")
                continue
                pass
            latest_file = max(list_of_files,key=os.path.getctime)
            filename = latest_file
            # print('Got filename ' + filename)
            frame_time = cuav_util.parse_frame_time(filename)
            # print "Got frame time %f on 2nd try" % frame_time
        except Exception:
            pass

    if last_frame_time == frame_time:
        raise chameleon.error("timeout waiting for fake image")
    last_frame_time = frame_time
    try:
        # print('loading image ' + filename)
        fake_img = load_image(filename)
    except Exception, msg:
        print('Error trying to load image')
        raise chameleon.error('missing %s' % fake)
    frame_counter += 1
    img.data = fake_img.data
    if continuous_mode:
        trigger_time = time.time()
    return trigger_time, frame_counter, 0

def close(h):
    return

def set_gamma(h, gamma):
    global chameleon_gamma
    chameleon_gamma = gamma

def set_framerate(h, framerate):
    global frame_rate
    frame_rate = framerate

def save_pgm(filename, img):
    return chameleon.save_pgm(filename, img)

def save_file(filename, bytes):
    return chameleon.save_file(filename, bytes)
