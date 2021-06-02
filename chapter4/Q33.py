from Q30 import trans_dict, parse

def extract(lines):
    noun = []
    for line in lines:
        for i in range(1, len(line)-1):
            if line[i-1]['pos'] == '名詞' and line[i]['surface'] == 'の' and line[i+1]['pos'] == '名詞':
                noun.append(line[i-1]['surface'] + line[i]['surface'] + line[i+1]['surface'])

    return noun

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    noun = extract(result)

    print(noun)
