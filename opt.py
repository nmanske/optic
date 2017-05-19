import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command', help='parse options of specified command')
parser.add_argument('options', help='learn more about these')
parser.add_argument('-a', '--all', help='display all available options',
                    action='store_true')
args = parser.parse_args()

cmd_in = args.command
opts_in = list(args.options.replace('-',''))

opts_dict = {}
syn_dict = {}
defs_dict = {}

# CONSTRUCT DICTIONARIES OF TARGET CMD
with open('definitions/' + cmd_in, 'r') as f:
    entries = f.read().split('\n\n')
    for index, entry in enumerate(entries, start=1):
        opts = entry.replace(',','').replace('-','').split('\n')[0].split(' ')
        for opt in opts:
            opts_dict.update({opt:index})
        syn_dict.update({index:entry.split('\n')[0]})
        defs = ' '.join(entry.split('\n')[1:])
        defs_dict.update({index:defs})

# FETCH OPTIONS IN USER GIVEN ORDER
for opt in opts_in:
    if opt in opts_dict:
        dict_index = opts_dict.get(opt)
        syn_entry = syn_dict.get(dict_index)
        dict_entry = defs_dict.get(dict_index)
        print(syn_entry + '\n' + dict_entry + '\n')
    else:
        print('-' + opt + '\ninvalid option\n')
