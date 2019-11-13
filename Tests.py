import os
import sys, getopt

def main(argv):
	if argv[1]:
		video_set_file = sys.argv[1]
		print('File to be read: {}'.format(video_set_file))
		fn = open(video_set_file)
		n = 1
		for aLine in fn:
			print('Line: {}:{}'.format(n, aLine))
			if (aLine[:1] == '#'):
				print('\t-- SKIPPING --')
				continue
			n += 1

		print('Counted {} uncommented lines'.format(n))

if __name__ == "__main__":
    print('sys.argv: {}'.format(sys.argv))
    main(sys.argv)
