from Q30 import trans_dict
from Q35 import word_counter
import collections
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
#import japanize_matplotlib

sns.set(font='IPAGothic')

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('--q39', help = 'image file for Q39')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = parse()
    with open(args.file, 'r') as f:
        lines = f.read().split('EOS\n')

    lines = list(filter(lambda x: x != '', lines))
    result = [trans_dict(line) for line in lines]

    num = [x[1] for x in word_counter(result).most_common()]

    fig = plt.figure()

    plt.scatter(np.log(range(1, len(num)+1)), np.log(num))
    plt.show()

    fig.savefig(args.q39)
