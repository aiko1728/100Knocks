import collections
from Q30 import trans_dict

def word_counter(lines):
    tmp = []
    for line in lines:
        for i in range(len(line)):
            tmp.append(line[i]['base'])
    result = collections.Counter(tmp)            
    
    return result

with open('neko.txt.mecab', 'r') as f:
    lines = f.read().split('EOS\n')

lines = list(filter(lambda x: x != '', lines))
result = [trans_dict(line) for line in lines]

num = word_counter(result)

print(num)