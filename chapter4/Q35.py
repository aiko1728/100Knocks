import collections
from Q30 import trans_dict, parse

def word_counter(lines):
    tmp = []
    for line in lines:
        for i in range(len(line)):
            tmp.append(line[i]['base'])
    result = collections.Counter(tmp)            
    
    return result

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    num = word_counter(result)

    print(num)
