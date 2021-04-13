import re

def trans_dict(line):
    line_list = []
    for word in line.split('\n'):
        data = re.split('[\t|,]', word)
        if len(data) < 5:
            continue
        word_dict = {'surface' : data[0], 'base' : data[7], 'pos' : data[1], 'pos1' : data[2]}
        line_list.append(word_dict)

    return line_list


if __name__ == '__main__':
    with open('neko.txt.mecab', 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]