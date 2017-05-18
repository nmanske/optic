import sys

cmd = sys.argv[1]

with open('definitions/' + cmd, 'r') as opt_list:
    opt = opt_list.read()

print(opt)
