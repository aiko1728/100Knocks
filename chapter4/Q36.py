from Q30 import trans_dict
from Q35 import word_counter
import collections
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
#import japanize_matplotlib

sns.set(font='IPAGothic')

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('--q36', help = 'image file for Q36')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    num = word_counter(result)

    word_list = list(zip(*num.most_common(10)))

    t = word_list[0]
    s = word_list[1]

    fig = plt.figure()

    plt.bar(t, s)
    plt.show()

    fig.savefig(args.q36)
