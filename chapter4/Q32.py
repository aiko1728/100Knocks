from Q30 import trans_dict

def extract(lines):
    base = []
    for line in lines:
        _list = list(filter(lambda x: x['pos'] == '動詞', line))

        for word in _list:
            base.append(word['base'])

    return base

with open('neko.txt.mecab', 'r') as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
result = [trans_dict(line) for line in lines]

base = extract(result)

print(base)