from Q30 import trans_dict
import collections
import matplotlib.pyplot as plt
import seaborn as sns
#import japanize_matplotlib

sns.set(font='IPAGothic')

def counter(lines):
    tmp = []
    for line in lines:
        for word in line:
            tmp.append(word['base'])
    result = collections.Counter(tmp)            
    
    return result

with open('neko.txt.mecab', 'r') as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
result = [trans_dict(line) for line in lines]

num = counter(result)

fig = plt.figure()

plt.hist(num.values(),bins=10,range=(1,10))
plt.show()

fig.savefig('hist.png')