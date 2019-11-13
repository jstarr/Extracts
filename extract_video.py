#!/usr/bin/python3

""" Extract portions from as many files as planned.
    For each video segment you will be asked for:
        1) 00:start:time,
        2) 00:end:time
        3) the /original/file/path,
        4) output/file/path,
"""
import os
import sys, getopt
# from datetime import datetime
import datetime

def main(argv):
    print('Arguments: {}'.format(argv))
    fmt = '%H:%M:%S'
    start_time = 0
    source_video = 2
    dest_video = 3

    video_set_file = '/home/linaro/Videos/videosets.csv'
    if argv[1]:
        video_set_file = argv[1]

    print('File to be read: {}'.format(video_set_file))
    fn = open(video_set_file)
    nLines = 0
    skipped_files = 0
    tot_screen_time = datetime.timedelta(microseconds=0)
    for aLine in fn:
        nLines += 1
        #   Lines beginning with a # are skipped
        if (aLine[:1] ==  '#'):
            print('-- SKIPPING --')
            skipped_files += 1
            continue
        this_set = aLine.split(',')
        print('Parsed:{}'.format(this_set))

        #   Do the real work
        diff = datetime.datetime.strptime(this_set[1].lstrip(), fmt) - datetime.datetime.strptime(this_set[0].lstrip(), fmt)
        tot_screen_time = tot_screen_time + diff
        print('Diff: {}\tTotal time: {}'.format(diff, tot_screen_time))
        c = "ffmpeg -ss {start} -i {input} -vcodec copy -t {length} {output}"
        copy_cmd = c.format(start=this_set[start_time],
                        input=this_set[source_video],
                        length=diff,
                        output=this_set[dest_video])
        print('The Command: {}'.format(copy_cmd))

        returned_value = os.system(copy_cmd)  # returns the exit code in unix
        print('returned value:', returned_value)
        print('\n\n')

    print('Total time: {}'.format(tot_screen_time))

if __name__ == "__main__":
    print('sys.argv: {}'.format(sys.argv))
    main(sys.argv)
