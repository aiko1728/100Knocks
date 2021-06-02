from Q30 import trans_dict, parse

def extract(lines):
    base = []
    for line in lines:
        word_list = list(filter(lambda x: x['pos'] == '動詞', line))

        for word in word_list:
            base.append(word['base'])

    return base

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    base = extract(result)

    print(base)
