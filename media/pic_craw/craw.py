import os
import pandas as pd

temp=[]
df=pd.read_excel('pic_craw/out_id.xlsx')
line=0
for i in range(len(df.index.values)):
    data=df.iloc[i,1]
    if(data==''):
        continue
    line+=1
    print(line)
    list=data.split('\t')
    print(len(list))
    for l in range(len(list)):
        temp.append(list[l])
        print(temp[i])

print(len(temp))

for i in range(len(temp)):
    img_name=temp[i]
    source_path='./MCG-FNeWS18/task3/train/rumor_pic/'+img_name
    print(source_path)
    if(os.path.exists(source_path)==False):
        continue
    dest_path='nanqiong/dest/'+img_name
    img_src=open(source_path,'rb')
    content=img_src.read()
    img_copy=open(dest_path,'wb')
    img_copy.write(content)
    img_src.close()
    img_copy.close()
