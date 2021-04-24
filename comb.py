import pandas as pd
import itertools
import re

df = pd.read_csv('data.csv')
dfk = pd.read_csv('key.csv')

print(df)

# # print(dfk)
# print(list(itertools.combinations(dfk['Issue'], 3)))

comb = list(itertools.combinations(dfk['Issue'], 2))

counter = 0
arr = []
rep = 0
maxcoDesc = str()
maxcoRep = 0
for x in comb:
    for item in df['Desc']:
        for y in x:
            if re.search(y, item) is not None:
                counter = counter + 1
                # print(re.search(y, item))
                # print(str(len(x)) + ' = ' + str(counter))
            else:
                counter = 0
                break
        if counter == len(x):
            # print('True')
            rep = rep + 1
        counter = 0
    print(str(x) + ' : ' + str(rep))
    rep = 0
