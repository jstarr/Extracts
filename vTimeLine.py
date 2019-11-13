#!/usr/bin/python3

""" Contain the data in a line of video time data
"""
import os
import sys, getopt
from datetime import datetime

def convertTo_date_time(myTime):
    return datetime.datetime.combine(datetime.date.today(), myTime)

class video_time_line:

    def __init__(self,
                 fmt='%H:%M:%S',
                 start_time=None,
                 end_time=None,
                 source_file_name=None,
                 dest_file_name=None
                ):
        self.vFmt(fmt)
        self.vstart_time(start_time)
        self.vend_time(end_time)
        self.vsource_file_name(source_file_name)
        self.vdest_file_name(dest_file_name)

    def vstart_time(self, myTime=None):
        if myTime:
            self._startTime = datetime.strptime(myTime.strip(), self._fmt)
        return self._startTime

    def vend_time(self, myTime=None):
        if myTime:
            # myTimeParts = myTime.strip().split(':')
            self._endTime = datetime.strptime(myTime.strip(), self._fmt)
            # self._endTime = datetime(int(myTimeParts[0]),
            #                      int(myTimeParts[1]),
            #                      int(myTimeParts[2]))
        return self._endTime

    def vsource_file_name(self, myFileName=None):
        if myFileName:
            self._sourceFileName = myFileName.strip()
        return self._sourceFileName

    def vdest_file_name(self, myFileName=None):
        if myFileName:
            self._destFileName = myFileName.strip()
        return self._destFileName

    def vFmt(self, fmt=None):
        if fmt:
            self._fmt = fmt
        return self._fmt

    def vDelta(self):
        cDelta = self._endTime - self._startTime
        return cDelta

    def sDelta(self):
        """Return the difference as a string"""
        delta = self.vDelta()
        cDelta = '0{}'.format(delta)[:8]
        return cDelta
