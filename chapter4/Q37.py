from Q30 import trans_dict
import collections
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
#import japanize_matplotlib

sns.set(font='IPAGothic')

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('--q37', help = 'image file for Q37')

    args = parser.parse_args()

    return args

def neko_counter(lines):
    tmp = []
    for line in lines:
        if any(word['base'] == '猫' for word in line):
            for i in range(len(line)):
                if line[i]['base'] != '猫':
                    tmp.append(line[i]['base'])
    result = collections.Counter(tmp)            
    
    return result

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    num = neko_counter(result)

    word_list = list(zip(*num.most_common(10)))

    t = word_list[0]
    s = word_list[1]

    fig = plt.figure()

    plt.bar(t, s)
    plt.show()

    fig.savefig(args.q37)
