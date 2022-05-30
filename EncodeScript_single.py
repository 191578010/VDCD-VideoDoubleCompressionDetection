# -*- encoding: utf-8 -*-

import os

BIT_RATE = [300,500,700,800]

GOP_FIRST = [5]
# CMD_FIRST = 'ffmpeg -s cif -i %s -vcodec libx264 -profile baseline -b:v %dk -g %d -refs 1 -r 25 %s' # oldversion
# CMD_FIRST = 'ffmpeg -f rawvideo -pix_fmt yuv420p -s cif -i %s -vcodec mpeg2video -b:v %dk -bt %dk -sc_threshold 0 -g %d -refs 1 -r 25 %s' #newversion for mpeg 2
CMD_FIRST = 'ffmpeg -f rawvideo -pix_fmt yuv420p -s cif -i %s -vcodec libx264 -profile:v baseline -frames 250 -b:v %dk -sc_threshold 0 -g %d -refs 1 -r 25 %s' #newversion for mpeg 4

GOP_SECOND = [20]
#CMD_SECOND = 'ffmpeg -i %s -vcodec libx264 -profile baseline -b:v %dk -g %d -refs 1 -r 25 %s'
CMD_SECOND = 'ffmpeg -i %s -vcodec libx264 -profile:v baseline -b:v %dk -sc_threshold 0 -g %d -refs 1 -r 25 %s'

current_path = os.getcwd()
print current_path


# first round encode
for video_file in os.listdir(current_path):
    print video_file
    if os.path.isfile(os.path.join(current_path, video_file)):
        if video_file.find('.yuv') >= 0:
            for bit_rate in BIT_RATE:
                for gop in GOP_FIRST:
                    new_name = 'first/%s_%d_%dk.264' % (video_file[:video_file.find('.')], gop, bit_rate)
                    os.system(CMD_FIRST % (video_file, bit_rate, gop, new_name))

# second round encode
current_path += r'/first'
os.chdir(current_path)
for video_file in os.listdir(current_path):
    if os.path.isfile(os.path.join(current_path, video_file)):
        if video_file.find('.264') >= 0:
            for bit_rate in BIT_RATE:
                for gop in GOP_SECOND:
                    new_name = r'../second/%s_%d_%dk.264' % (video_file[:video_file.find('.')], gop, bit_rate)
                    print CMD_SECOND % (video_file, bit_rate, gop, new_name)
                    os.system(CMD_SECOND % (video_file, bit_rate, gop, new_name))
