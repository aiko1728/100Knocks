from Q30 import trans_dict, parse

def extract(lines):
    surface = []
    for line in lines:
        _list = list(filter(lambda x: x['pos'] == '動詞', line))

        for word in _list:
            surface.append(word['surface'])

    return surface


args = parse()
with open(args.file, 'r') as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
result = [trans_dict(line) for line in lines]

surface = extract(result)

print(surface)