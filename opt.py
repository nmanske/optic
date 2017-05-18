import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command', help='read options directory of specified command')
parser.add_argument('options', help='decipher options ')
parser.add_argument('-a', '--all', help='display all available options',
                    action='store_true')
args = parser.parse_args()

if args.command:
    print('FOUND - args.command [' + args.command + ']')
if args.options:
    print('FOUND - args.options [' + args.options + ']')
if args.all:
    print('FOUND - args.all [' + args.all + ']')
print()

cmd = sys.argv[1]
opts = list(sys.argv[2].replace('-',''))

with open('definitions/' + args.command, 'r') as f:
    definitions = f.read().split('\n\n')
    for entry in definitions:
        opts_line = entry.split('\n')[0]
        for opt in opts:
            if opt in opts_line:
                print(entry+'\n')
                opts.remove(opt)
for unknown_opt in opts:
    print('Unknown option -' + unknown_opt)
