#usr/bin/env/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action='store_true')
args = parser.parse_args()
if args.version:
	print('This is test version 0.1.')

parser = argparse.ArgumentParser()
parser.add_argument('--width', '-w', help='set output width')
args = parser.parse_args()
if args.width:
	print('set output width to %s' % args.width)
