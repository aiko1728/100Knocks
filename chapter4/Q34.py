from Q30 import trans_dict, parse

def extract(lines):
    noun = []
    tmp = []
    for line in lines:
        for i in range(len(line)):
            if line[i]['pos'] == '名詞':
                tmp.append(line[i]['surface'])
            elif len(tmp) >= 2:
                noun.append(''.join(tmp))
                tmp = []
            else:
                tmp = []
                
    return noun

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    noun = extract(result)

    print(noun)
