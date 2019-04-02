#!/usr/bin/env python
# coding: utf-8


with open('/Users/kzhao46/Downloads/628-2/data/review_train.json', "r", encoding="utf-8") as f:
    with open('/Users/kzhao46/Downloads/628-2/data/review_train.csv', "w", encoding="utf-8") as f2:
        i = 0
        for line in f:
            temp = json.loads(line.rstrip())
            tdata = pd.DataFrame(temp, index = [i])
           # temp = pd.DataFrame(json.loads(line.rstrip()), index = [i])
         #   print(tdata)
          #  print(tdata.loc[0])
            f2.write((str(tdata.loc[i][0]) + ',' + str(tdata.loc[i][1]) + ',' + tdata.loc[i][3] + '\n'))
            i = i + 1
            if i%100000==0:
                print(i)





