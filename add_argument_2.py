#usr/bin/env/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--width', '-w', help='set output width')
args = parser.parse_args()
if args.width:
	print('set output width to %s' % args.width)
