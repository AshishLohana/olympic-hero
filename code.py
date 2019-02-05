# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file

data = pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"}, inplace = True)
print(data.head(10))

#Code starts here



# --------------
#Code starts here




data['Better_Event'] = np.where((data['Total_Summer'] > data['Total_Winter']),'Summer',(np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both')))


#data['Better_Event'] = np.where((data['Total_Summer'])>(data['Total_Winter']),'summer', np.where((data['Total_Summer'])<(data['Total_Winter']),'winter','both'))


#data['Better_Event'] = np.where(data['Total_Summer']<data['Total_Winter'],'Winter')
#data['Better_Event'] = np.where(data['Total_Summer']=data['Total_Winter'],'Both')

#print("w={} s={} ={}".format(data['Total_Winter'],data['Total_Summer'],
#print(data['Better_Event'])
better_ = data['Better_Event'].value_counts()
print(type(better_))
better_event = better_.argmax()
print(better_event)



# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[len(top_countries)-1],inplace=True)

#def top_ten(top_countries,column_):
#    country_list = []
#    t = column_.nlargest(10)
#    for i in column_:
#        country_list.append(i.arg())
#    return country_list
#print(country_list)
def top_ten(top_,column_):
    country_list = []
    t = top_.nlargest(10,column_)
    print(t)
    print("top ten countries: ")
    print(list(t['Country_Name']))
    country_list = list(t['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')

top_10_winter = top_ten(top_countries,'Total_Winter') 

top_10 =  top_ten(top_countries,'Total_Medals')

common = []
for i in top_10_summer:
    if ((i in top_10_winter) & (i in top_10)):
        common.append(i)
print(common)






# --------------
#Code starts here




summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

print(" summer medalists: ",summer_df)
print(" winter medalists: ",winter_df)
print(" top medalists: ",top_df)

plt.bar(x = summer_df['Country_Name'],height=summer_df['Total_Summer'])
plt.bar(x = winter_df['Country_Name'],height=winter_df['Total_Winter'])
plt.bar(x = top_df['Country_Name'],height=top_df['Total_Medals'])


# --------------
#Code starts here




summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df['Country_Name'][summer_df['Golden_Ratio'].argmax()]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/summer_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio'].argmax()]

top_df['Golden_Ratio'] = top_df['Gold_Total']/summer_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio'].argmax()]




# --------------
#Code starts here

data = pd.read_csv(path)
data_1 = data
data_1.drop((len(data_1)-1),axis=0,inplace=True)
print(data_1)

#data_1['Total_Points'] = [data_1['Gold_Total']*3] + [data_1['Silver_Total']*2] + data_1['Bronze_Total']
data_1['Gold_Total'] = 3 * (data_1['Gold_Total'])
data_1['Silver_Total'] = 2 * data_1['Silver_Total']

data_1['Total_Points'] = data_1['Gold_Total'] + data_1['Silver_Total']  + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
best_country = data_1['Country_Name'][data_1['Total_Points'].argmax()]




# --------------
#Code starts here





best_ = data_1[data_1['Country_Name'] == best_country]

best = best_[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


