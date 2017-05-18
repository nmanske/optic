import sys

def main():
    cmd = sys.argv[1]
    opts = list(sys.argv[2].replace('-',''))
    with open('definitions/' + cmd, 'r') as f:
        definitions = f.read().split('\n\n')
        for entry in definitions:
            opts_line = entry.split('\n')[0]
            for opt in opts:
                if opt in opts_line:
                    print(entry+'\n')
                    opts.remove(opt)
    for unknown_opt in opts:
        print('Unknown option -' + unknown_opt)

if __name__ == '__main__':
    main()
