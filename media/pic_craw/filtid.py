import pandas as pd
import os.path
import re

writer=pd.ExcelWriter('out_id.xlsx')
temp=[]
df=pd.read_excel('train.xlsx')

# for i in range(len(df.index.values)):
#     if(df.iloc[i,5]==1 and df.iloc[i,2]!='[]'):

#         temp.append(df.iloc[i,0])

for i in range(5):
    if(df.iloc[i,5]==1 and df.iloc[i,2]!='nan'):
        path=df.iloc[i,2]
        path_list=path.split(' ')
        length=len(path_list)
        for j in range(length):
            # temp_path=path_list[j]
            # spath=temp_path.rsplit("/",1)
            # img_path=spath[1]
            # print(img_path.split('\'')[0])
            print(path_list[j])
            temp.append(path_list[j])


# df2=pd.DataFrame(data=temp)
# df2.to_excel(writer)
# writer.save()