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
    parser.add_argument('--q38', help = 'image file for Q38')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    num = word_counter(result)

    fig = plt.figure()

    plt.hist(num.values(),bins=10,range=(1,10))
    plt.show()

    fig.savefig(args.q38)
