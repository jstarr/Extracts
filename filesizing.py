#!/usr/bin/python3
"""Calculate the total time for the output files"""
from vTimeLine import video_time_line
import os
import os.path
from os import path
import sys, getopt
import datetime

def main(argv):
    # Initializations
    fmt = '%H:%M:%S'
    jstartTime = 0
    jendTime = 1
    jsourceVideo = 2
    jdestVideo = 3
    totScreenTime = datetime.timedelta(microseconds=0)
    totFileSize = 0
    nLines = 0
    skippedFiles = 0

    video_set_file = '/home/linaro/Videos/videosets.csv'
    if argv[1]:
        video_set_file = argv[1]

    fn = open(video_set_file)
    for aLine in fn:
        nLines += 1
        #   Lines beginning with a # are skipped
        if (aLine[:1] ==  '#'):
            skippedFiles += 1
            continue
        thisSet = aLine.split(',')
        aTimeLine = video_time_line(start_time=thisSet[jstartTime], end_time=thisSet[jendTime], source_file_name=thisSet[jsourceVideo], dest_file_name=thisSet[jdestVideo])

        #   Do the real work
        diff = aTimeLine.vDelta()
        totScreenTime = totScreenTime + diff
        destination = aTimeLine.vdest_file_name()
        fileSize = 0
        if path.exists(aTimeLine.vdest_file_name()):
            fileSize = path.getsize(destination)
            totFileSize += fileSize
        fields = 'Length: {}\tDestination: {:35s}\tTotal time: {}\tFile Size {:>20,d}'
        print(fields.format(aTimeLine.sDelta(),
                            aTimeLine.vdest_file_name(),
                            totScreenTime,
                            fileSize)
                           )

    print('\n\tTotal time: {0}\tTotal File Size:{1:>20,d}'.format(
                                                      totScreenTime,
                                                      totFileSize)
                                                    )

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('\n\nFile: {}\n'.format(sys.argv[1]))
        main(sys.argv)
    else:
        print('Usage:\tpython timing.py file_with_list_of_extracts.csv')
