# Name: Extracts
##  Extract pieces of a movie

Use this python application to extract a piece or pieces of a video file (as of 11/13/2019, only tested mp4 files and Python 3.6 & 3.7)

To use it, run
  > `extract_video.py` *comma_separated_file.csv*
  
  Where *comma_separated_file.csv* contains lines detailing where to get the source and where to put the output in the following format:
  
1. Starting Time from the beginning of the source file e.g. 00:00:10 would start 10 seconds into the source.

2. Ending Time from the beggining of the source file e.g. 00:01:10 would start 1 minute 10 seconds into the source.

3. Name of the source file e.g. ~/Videos/my_original.mp4
4. Name of the output file e.g. ~/Videos/my_output.mp4

NOTE: Any line beginning with a '#' is ignored.