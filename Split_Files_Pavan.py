import pandas as pd
import operator
#import dask.dataframe as dd

#from Utils.utilsparse import getcurrenttime
#getcurrenttime()

# TH_Product_3PA_A
# th_web_file_C
#pass below file paths to store 
#below test_sample is the file name

to_strorefile="C:\\Users\\abdul.yousuf\\Desktop\\New folder\\2020-03-06\AVLABL\\to_file\\test_sample"
#Read file Using Dask
fileToRead='th_web_file_C'
df_textdata1=pd.read_csv('C:\\Users\\abdul.yousuf\\Desktop\\New folder\\2020-03-06\\AVLABL\\'+fileToRead,delimiter="\t",header=None,engine='python')
#s=df_textdata1.size.compute()
#print(s)
#Convert Dask dataframe to pandas dataframe
#new_df1=df_textdata1.compute()
new_df1=df_textdata1
#Split dataframe to multiple dataframes
# For FC_product_3PA
#df1=new_df1[0:15986962]
#df2=new_df1[15986963:]

# For TH Web and Product 3PA
#to un coment remove below quotes starting and ending
'''
df1=new_df1[0:2656415]
df2=new_df1[2656416:5312830]
df3=new_df1[5312831:7969245]
df4=new_df1[7969246:10625660]
df5=new_df1[10625661:13282075]
df6=new_df1[13282076:]

#df3=new_df1[22986963:32986962]
#df4=new_df1[32986963:42986962]
#df5=new_df1[42986963:52986962]
#df6=new_df1[52986963:]

print(df1.shape)
#getcurrenttime()

#Save dataframes to file
df1.to_csv(to_strorefile+fileToRead+'_1',index=False)
df2.to_csv(to_strorefile+fileToRead+'_2',index=False)
df3.to_csv(to_strorefile+fileToRead+'_3',index=False)
df4.to_csv(to_strorefile+fileToRead+'_4',index=False)
df5.to_csv(to_strorefile+fileToRead+'_5',index=False)
df6.to_csv(to_strorefile+fileToRead+'_6',index=False)
'''

#below logic is for promotion level to execute remove the quotes below


lst=new_df1[new_df1[0].str.contains('PLD\+')].index

pld_index=list(lst)

check=0

prev_index=0

if len(pld_index)==1:
    
    test_df=new_df1[prev_index:]
    test_df.to_csv(to_strorefile+"_"+str(i),index=False)
else:
    pld_index=pld_index[1:]
    for i in pld_index:
        test_df=new_df1[prev_index:i]
        test_df.to_csv(to_strorefile+"_"+str(i),index=False)
        prev_index=i


#getcurrenttime()