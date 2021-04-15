from Q30 import trans_dict, parse
import collections
import matplotlib.pyplot as plt
import seaborn as sns
#import japanize_matplotlib

sns.set(font='IPAGothic')

def word_counter(lines):
    tmp = []
    for line in lines:
        for i in range(len(line)):
            tmp.append(line[i]['base'])
    result = collections.Counter(tmp)            
    
    return result

args = parse()
with open(args.file, 'r') as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
result = [trans_dict(line) for line in lines]

num = word_counter(result)

_list = list(zip(*num.most_common(10)))

t = _list[0]
s = _list[1]

fig = plt.figure()

plt.bar(t, s)
plt.show()

fig.savefig(args.q36)