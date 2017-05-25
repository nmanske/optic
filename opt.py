import sys
import argparse
import os
import re

# Parse and assign user input
parser = argparse.ArgumentParser()
parser.add_argument('command', help='parse options of specified command')
parser.add_argument('options', help='learn more about these', nargs='+')
parser.add_argument('-a', '--all', help='display all available options',
                    action='store_true')
parser.add_argument('-s', '--short', help='interpret all options as short-form',
                    action='store_true')
parser.add_argument('-l', '--long', help='interpret all options as long-form',
                    action='store_true')
parser.add_argument('-k', '--keyword', help='find option based on search word',
                    action='store_true')

args = parser.parse_args()
cmd_in = args.command
opts_in = args.options

# Check that parsed command has definition
cmd_defs = os.listdir('definitions')
if cmd_in not in cmd_defs:
    print(cmd_in + ' does not have a definition')
    sys.exit(0)

# Construct master list of cmd definitions
entries_list = []
with open('definitions/' + cmd_in, 'r') as f:
    entries = f.read().split('\n\n')
    for index, entry in enumerate(entries, start=1):
        opts = entry.replace(',','').split('\n')[0].split(' ')
        altr = entry.split('\n')[0]
        defn = ' '.join(entry.split('\n')[1:])
        for opt in opts:
            opt_no_dash = re.sub('^[^a-zA-Z]*|[^a-zA-Z]*$', '', opt)
            entries_list.append((opt_no_dash, altr, defn))

# Fetch options in user given order
print(opts_in)
for opt_in in opts_in:
    #if any(entry[0] == opt_in and len(opt_in) > 1 for entry in entries_list):
    for entry in entries_list:
        opt = entry[0]
        if opt_in == opt:
            altr = entry[1]
            defn = entry[2]
            print(altr + '\n' + defn + '\n')
            break
    else:
        print('-' + opt_in + '\ninvalid option\n')
