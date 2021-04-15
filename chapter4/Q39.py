from Q30 import trans_dict, parse
import collections
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#import japanize_matplotlib

sns.set(font='IPAGothic')

def counter(lines):
    tmp = []
    for line in lines:
        for word in line:
            tmp.append(word['base'])
    result = collections.Counter(tmp)            
    
    return result

args = parse()
with open(args.file, 'r') as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
result = [trans_dict(line) for line in lines]

num = [x[1] for x in counter(result).most_common()]

fig = plt.figure()

plt.scatter(np.log(range(1, len(num)+1)), np.log(num))
plt.show()

fig.savefig('log.png')