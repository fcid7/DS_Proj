'''
Data Science Career Track (Springboard/DataCamp, 5/2018 - 1/2019) 
Topic: Capstone Project - 911 Police Calls for Service EDA, (Baltimore, MD) 
Student: Franklin Cid 
Mentor: Milad Toutounchian; milad.to@gmail.com
'''

 ## --------------- --------------- --------------- --------------- ---------------
 ## --------------- --------------- --------------- --------------- ---------------
 # 
 # 
 ## --------------- --------------- --------------- --------------- ---------------
'''
Github: https://github.com/fcid7/DS_Proj/settings/collaboration
Github: https://github.com/fcid7/DS_Proj/settings/collaboration

'''
 
#0 import packages/libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1 read 911 calls
c911 = pd.read_csv('Data/w911PoliceCalls_BaltimoreMD.csv')
# c911.head()
#assert pd.read_csv('Data/w911PoliceCalls_BaltimoreMD.csv')

#2 pull c911 into a df, drop unneeded columns
df911 = pd.DataFrame(c911, columns=['callDateTime', 'priority', 'district', 'description',
    'location'])
df911.head(6)

#3 cast callDateTime => dateTime (no date), new col
df911['dT'] =pd.to_datetime(df911.callDateTime) #, unit='s'
df911.head(6)

#3.a Set the index, Sort
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
df911.set_index('dT', drop=True)
df911.sort_values(by='dT', inplace=True)
df911.head(6)

#4 Now, pull only '01/2015', '01/2016', '01/2017'
''' Pull Months of Jan for 3 years (2015, 2016, 2017); Include needed cols
w911c = w911.callDateTime = '01/2017' #, '07/2017']]   #callDateTime [[01/2017, 07/2017]]
'''
df9115 = df911.loc[(df911.dT >= '01/2015') & (df911.dT < '02/2015')] #[df911.dT == '01/2017']
#df9115.tail() # 83994; location        83976

df9116 = df911.loc[(df911.dT >= '01/2016') & (df911.dT < '02/2016')]
#df9116.tail() #80087; location        78081

df9117 = df911.loc[(df911.dT >= '01/2017') & (df911.dT < '02/2017')] #[df911.dT == '01/2017']
df9117.tail() #84422; location        82645

#4.a Create New Col ('yr') in all df. Optional, as the final df () will only be used to aggregate counts.
#df9115['yr'] = '';  df9116['yr'] = '';  df9117['yr'] = ''
#df9115.yr = pd.DatetimeIndex(df9115.dT).year  #df911A['dT'].year
#df9116.yr = pd.DatetimeIndex(df9116.dT).year  #df911A['dT'].year
#df9117.yr = pd.DatetimeIndex(df9117.dT).year  #df911A['dT'].year
#err: A value is trying to be set on a copy of a slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value instead
#df9116.tail() # 83994; location        83976

#5 Concat 3 dfs. Add 4 new columns. Calc yr as .year part. Name column clearly.
df9115.columns = df9115.columns.str.replace('description','callType')
df9116.columns = df9116.columns.str.replace('description','callType')
df9117.columns = df9117.columns.str.replace('description','callType')

df911A = pd.concat([df9115, df9116, df9117]) #, ignore_index=True); 248503/244702=loc
df911A.columns = df911A.columns.str.replace('description','callType')
df911A['yr'] = ''; 
df911A['street'] = ''; 
df911A['cityState'] = ''; 
df911A['latLong'] = ''
df911A.yr = pd.DatetimeIndex(df911A.dT).year  #df911A['dT'].year
df911A.head()

#6 Calc 3 cols by parsing from location
df911A['street'] = df911A.location.str.split('\n').str[0]
df911A['cityState'] = df911A.location.str.split('\n').str[1]
df911A['latLong'] = df911A.location.str.split('\n').str[2]
df911A.head()

#7 Get the counts of variables using yr+priority, yr+callType, yr+district
# 7.a Check groups as:
dfP = df911A.groupby(['yr', 'priority']).count()

# 7.b Check groups as:
dfC = df911A.groupby(['yr', 'callType']).count()

# 7.c Check groups as:
dfD = df911A.groupby(['yr', 'district']).count()

### In Progress...In Progress...In Progress...In Progress...In Progress... 
### In Progress...In Progress...In Progress...In Progress...In Progress... 
### In Progress...In Progress...In Progress...In Progress...In Progress... 

plt.plot(dfP.index, dfP.loc[dfP.priority == 'High'], color='red', label='Priority')
#plt.plot(df9115.yr, df9115.priority, color='red', label='Priority')
#plt.plot(df9116.yr, df9116.priority, color='green', label='Priority')
#plt.plot(df9117.yr, df9117.priority, color='blue', label='Priority')
plt.title('911 Police Calls - Priority by Year')
plt.ylabel('Priority')
plt.xlabel('Year')
plt.legend(loc='lower right')
plt.show()


plt.figure(figsize=(12,8)) #callDateTime district callType location dT street cityState latLong
sns.lmplot(dfP, time='yr', unit = "priority", condition='priority', value='callDateTime')
plt.show()


### ===========   ===========   ===========   ===========   ===========   
#7 Data Wrangling. Check empty, NaN/NULL
### DATA WRANGLING. Data Wrangling. Check empty, NaN/NULL
#df911A.loc[df911A.yr == 2015].count()
#df911A.loc[df911A.yr == 2016].count()
#df911A.loc[df911A.yr == 2017].count()
df9117 = df911A.loc[df911A.yr == 2017]
df9117.head(14)

df9117w = df9117.loc[df9117.district == 'CD']
df9117w.head(14)

### <END> ===========   ===========   ===========   ===========   ===========
### <END> ===========   ===========   ===========   ===========   ===========






