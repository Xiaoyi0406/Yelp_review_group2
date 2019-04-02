#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import math
#from mpl_toolkits.basemap import Basemap
from matplotlib import cm
import seaborn as sns
from sklearn.decomposition import LatentDirichletAllocation


# In[8]:


f = pd.read_csv( '/Users/kzhao46/Dropbox/628-2/data/business_train.csv',encoding='latin-1')


# In[3]:


bool = f['name']=='Swiss Chalet Rotisserie & Grill'
f[bool.values==True].head(3)


# In[4]:


id = f[bool.values==True]['business_id']
#id.to_csv("id.csv")
swiss = pd.read_csv('id.csv',encoding='latin-1').head()


# In[5]:


#id[514]


# In[10]:


data_file = '/Users/zzz/Desktop/STAT628/Module 2/Data/review_train.json'

r_sample = []
with open(data_file, 'r') as f:
    r_sample.append(f.readlines())

r_sample = r_sample[0]
review = []
for i in range(0,len(r_sample)):
    r_review = json.loads(r_sample[i])
    if r_review['business_id'] in id:
        review.append(r_review)

f.info()f1 = f.iloc[:,lambda df:[0,1,2,3,4,5,6,7,8,26]] 
f1.head(10)
#f1cat=f1['categories']
cat.head(10)
# In[ ]:


bool = cat.str.contains('.Restaurants.') #不要忘记正则表达式的写法，'.'在里面要用'\.'表示
print('bool : \n', bool.head(10),)


# In[ ]:





# In[ ]:


cat[bool.values==True].head(10)


# In[ ]:


cat[bool.values==True].count()


# In[ ]:


restaurant = f1[bool.values==True]
restaurant.head(6)


# In[ ]:


restaurant.info()


# Now we get all data of restaurants, and we want all restaurants in US.

# In[ ]:


r_postc = restaurant['postal_code']
r_postc.head(8)


# In[ ]:


bool = r_postc.str.contains(r'\d{5}') #不要忘记正则表达式的写法，'.'在里面要用'\.'表示
print('bool : \n', bool.head(10),)


# In[ ]:


r_us = restaurant[bool.values==True]
r_us.head(5)
#r_us


# In[ ]:


r_us.info()


# Then we want to have a look at the positions of these restaurants in US.

# In[9]:


from mpl_toolkits.basemap import Basemap
from matplotlib import cm


# In[ ]:


map = Basemap(projection='stere',lat_0=90,lon_0=-105,            llcrnrlat=23.41 ,urcrnrlat=45.44,            llcrnrlon=-118.67,urcrnrlon=-64.52,            rsphere=6371200.,resolution='l',area_thresh=10000)
map.drawmapboundary()
#map.drawmapboundary(fill_color = 'skyblue')   # 绘制边界
#map.fillcontinents(color = 'coral') # 填充大陆，发现填充之后无法显示散点图，应该是被覆盖了
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
#map.drawcounties()      # 绘制县
parallels = np.arange(0.,90,10.) 
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线
meridians = np.arange(-110.,-60.,10.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线
lat = np.array(r_us['latitude'])
lon = np.array(r_us['longitude'])
x,y = map(lon,lat)
map.scatter(x,y,color = 'red', marker = 'o')    
plt.title('Restaurants in America')
plt.show()


# In[ ]:


print(r_us['state'].unique(),len(r_us['state'].unique()))


# Take IL as an example:

# In[ ]:


r_il = r_us.loc[r_us['state']=='IL']
r_il.head(3)


# In[ ]:


map = Basemap(projection='stere',lat_0=40,lon_0=-89,            llcrnrlat=37 ,urcrnrlat=43,            llcrnrlon=-95,urcrnrlon=-80,            rsphere=6371200.,resolution='l',area_thresh=10000)
map.bluemarble()
#map.shadedrelief()
#map.etopo()
map.drawstates()
map.drawrivers(linewidth=0.5,color="blue")
lat = np.array(r_il['latitude'])
lon = np.array(r_il['longitude'])
x,y = map(lon,lat)
map.scatter(x,y)    
plt.show()


# In[ ]:


map = Basemap(projection='stere',lat_0=40,lon_0=-89,            llcrnrlat=37 ,urcrnrlat=43,            llcrnrlon=-95,urcrnrlon=-80,            rsphere=6371200.,resolution='l',area_thresh=10000)
map.drawmapboundary()   # 绘制边界
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
parallels = np.arange(30,50,1) 
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线
meridians = np.arange(-100.,-80.,1.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线
lat = np.array(r_il['latitude'])
lon = np.array(r_il['longitude'])
x,y = map(lon,lat)
map.scatter(x,y)    
plt.title('Restaurants in Ilinois')
plt.show()


# In[ ]:


from folium import plugins
import folium
import os
m = folium.Map([40.06, -88.16], zoom_start=13)  #中心区域的确定

lat = np.array(r_il['latitude'])
lon = np.array(r_il['longitude'])
nom = np.array(r_il['name'])

for i in range(len(lat)):
    folium.Marker([lat[i],lon[i]],popup=nom[i]).add_to(m)

m.save('map1.html') 


# In[ ]:


len(r_il['name'])-len(r_il['name'].unique())


# In[ ]:


for item in set(r_il['name']):
        if list(r_il['name']).count(item) > 1:
            print("the %s has found %d" %(item,list(r_il['name']).count(item)))


# In[ ]:


#set(nom)
#But also we find an 'McDonalds'
bool = r_il['name'] =='McDonalds'
r_il[bool.values==True]


# Then I want to see the details of McDonald's, Dairy Queen and Subway.

# In[ ]:


bool = r_il['name'].str.contains('McDonald.') 
r_Mc = r_il[bool.values==True]
r_Mc


# In[ ]:


id = list(r_Mc['business_id'])
f_Mc = f[f['business_id'].isin(id)]
f_Mc.head(3)


# In[ ]:


#f_Mc.to_csv('f_Mc.csv')


# In[ ]:


bool = r_Mc['is_open']==0
r_Mc[bool.values == True]
c_lat = np.array(r_Mc[bool.values == True]['latitude'])
c_lon = np.array(r_Mc[bool.values == True]['longitude'])
c_nom = np.array(r_Mc[bool.values == True]['name'])
#But we checked these closed shop, some of them weren't closed.


# In[ ]:


from folium import plugins
import folium
import os
m = folium.Map([40.06, -88.16], zoom_start=13)  #中心区域的确定

lat = np.array(r_il['latitude'])
lon = np.array(r_il['longitude'])
nom = np.array(r_il['name'])

for i in range(len(lat)):
    folium.Marker([lat[i],lon[i]],popup=nom[i]).add_to(m)

lat2 = np.array(r_Mc['latitude'])
lon2 = np.array(r_Mc['longitude'])
nom2 = np.array(r_Mc['name'])

for i in range(len(lat2)):
    folium.Marker([lat2[i],lon2[i]],popup=nom2[i],icon=folium.Icon(color='red')).add_to(m)   


for i in range(len(c_lat)):
    folium.Marker([c_lat[i],c_lon[i]],popup=c_nom[i],icon=folium.Icon(color='black')).add_to(m)   
    
m.save('IL_Mc_map.html') 


# In[ ]:


from folium import plugins
import folium
import os
m = folium.Map([40.06, -88.16], zoom_start=13)  #中心区域的确定

lat2 = np.array(r_Mc['latitude'])
lon2 = np.array(r_Mc['longitude'])
nom2 = np.array(r_Mc['name'])


for i in range(len(c_lat)):
    folium.Marker([c_lat[i],c_lon[i]],popup=c_nom[i],icon=folium.Icon(color='black')).add_to(m)   

for i in range(len(lat2)):
    folium.Marker([lat2[i],lon2[i]],popup=nom2[i],icon=folium.Icon(color='red')).add_to(m)   

#24/7
folium.Marker([40.09752068, -88.24523903],popup=nom2[i],icon=folium.Icon(color='green')).add_to(m)  
folium.Marker([40.11042079, -88.22974501],popup=nom2[i],icon=folium.Icon(color='green')).add_to(m)  
folium.Marker([40.13351546, -88.25956913],popup=nom2[i],icon=folium.Icon(color='green')).add_to(m)  


m.save('IL_Mconly_map.html') 


# In[ ]:


#f_Mc.info()
for i in range(len(lat2)):
    print([lat2[i],lon2[i]]) 


# In[ ]:


f_Mc_2 = f_Mc.iloc[:,lambda df:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,48,49,50,51,52,53,54]] 
f_Mc_2.head(3)


# Then I want to analyze the range of price.

# In[ ]:


bool = r_il['attributes.RestaurantsPriceRange2']=='1'
il_p1 = r_il[bool.values == True]


# In[ ]:


bool = r_il['attributes.RestaurantsPriceRange2']=='2'
il_p2 = r_il[bool.values == True]


# In[ ]:


bool = r_il['attributes.RestaurantsPriceRange2']=='3'
il_p3 = r_il[bool.values == True]


# In[ ]:


bool = r_il['attributes.RestaurantsPriceRange2']=='4'
il_p4 = r_il[bool.values == True]


# In[ ]:


bool = r_il['attributes.RestaurantsPriceRange2'].isnull()== True
il_p5 = r_il[bool.values == True]


# In[ ]:


from folium import plugins
import folium
import os
m = folium.Map([40.06, -88.16], zoom_start=13)  #中心区域的确定

lat1 = np.array(il_p1['latitude'])
lon1 = np.array(il_p1['longitude'])
nom1 = np.array(il_p1['name'])
pr1 = np.array(il_p1['attributes.RestaurantsPriceRange2'])

lat2 = np.array(il_p2['latitude'])
lon2 = np.array(il_p2['longitude'])
nom2 = np.array(il_p2['name'])

lat3 = np.array(il_p3['latitude'])
lon3 = np.array(il_p3['longitude'])
nom3 = np.array(il_p3['name'])

lat4 = np.array(il_p4['latitude'])
lon4 = np.array(il_p4['longitude'])
nom4 = np.array(il_p4['name'])

lat5 = np.array(il_p5['latitude'])
lon5 = np.array(il_p5['longitude'])
nom5 = np.array(il_p5['name'])


for i in range(len(lat1)):
    folium.Marker([lat1[i],lon1[i]],popup=nom1[i],icon=folium.Icon(color='orange')).add_to(m)   

for i in range(len(lat2)):
    folium.Marker([lat2[i],lon2[i]],popup=nom2[i],icon=folium.Icon(color='pink')).add_to(m)   

for i in range(len(lat3)):
    folium.Marker([lat3[i],lon3[i]],popup=nom3[i],icon=folium.Icon(color='red')).add_to(m)   
    
for i in range(len(lat4)):
    folium.Marker([lat4[i],lon4[i]],popup=nom4[i],icon=folium.Icon(color='blue')).add_to(m)   

for i in range(len(lat5)):
    folium.Marker([lat5[i],lon5[i]],popup=nom5[i],icon=folium.Icon(color='black')).add_to(m)   

m.save('IL_Pricerange_map.html') 


# In[ ]:


id = list(il_p3['business_id'])
f_p3 = f[f['business_id'].isin(id)]
f_p3.head(3)


# In[ ]:


#f_p3.to_csv('f_p3.csv')


# In[ ]:





# Then I want to deal with the reviews.
reviews = pd.read_csv('/Users/zzz/Dropbox/未命名文件夹/data/review_train.csv', header = 0)
#reviews.head(6)
reviews.columns = ['31292', '1', '5/7/2013 4:34']
# In[ ]:


data_file = '/Users/zzz/Desktop/STAT628/Module 2/Data/review_train.json'

r_sample = []
with open(data_file, 'r') as f:
    r_sample.append(f.readlines(20000))

r_sample = r_sample[0]
r_text = []
for i in range(0,len(r_sample)):
    r_review = json.loads(r_sample[i])
    r_text.append(r_review["text"].lower())
    
    #print(r_text)

data_file = '/Users/zzz/Desktop/STAT628/Module 2/Data/review_train.json'

r_sample = []
with open(data_file, 'r') as f:
    r_sample.append(f.readline())

r_sample = r_sample[0]
r_text = []
for i in range(0,len(r_sample)):
    r_review = json.loads(r_sample[i])
    r_text.append(r_review["text"].lower())
    
    print(r_text)
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


f = pd.read_csv( '/Users/zzz/Dropbox/未命名文件夹/data/restaurant/all.csv',encoding = 'latin-1')


# In[4]:


f.head(3)


# In[5]:


#f.info()


# In[6]:


bool = f['name'].str.contains('McDonald.') 
mc = f[bool.values==True]
mc.head(6)


# In[ ]:





# In[7]:


map = Basemap(projection='stere',lat_0=90,lon_0=-105,            llcrnrlat=23.41 ,urcrnrlat=55.44,            llcrnrlon=-118.67,urcrnrlon=-44.52,            rsphere=6371200.,resolution='l',area_thresh=10000)
map.drawmapboundary(
#map.drawmapboundary(fill_color = 'skyblue')   # 绘制边界
#map.fillcontinents(color = 'coral') # 填充大陆，发现填充之后无法显示散点图，应该是被覆盖了
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
#map.drawcounties()      # 绘制县
parallels = np.arange(0.,90,10.) 
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线
meridians = np.arange(-110.,-60.0.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线
lat = np.array(mc['latitude'])
lon = np.array(mc['longitude'])
x,y = map(lon,lat)
map.scatter(x,y,color = 'red', marker = 'o')    
plt.title('McDonald\'s in North America')
plt.show()


# In[35]:


bool = mc['circle'] == '1' 
mc_in = mc[bool.values==True]
mc_in.head(6)
#len(mc_in) 86


# In[36]:


mcin = pd.DataFrame(mc_in.iloc[:,lambda df:[6,7]] ,dtype=np.float)
mcin.head(3)


# In[37]:


bool = mc['circle'] == '0' 
mc_out = mc[bool.values==True]
#mc_out.head(6)
mcout = pd.DataFrame(mc_out.iloc[:,lambda df:[6,7]] ,dtype=np.float)
mcout.head(3)


# In[38]:


from folium import plugins
import folium
import os

m = folium.Map([40, -100], zoom_start=5)  #中心区域的确定

lat = np.array(mcin['latitude'])
lon = np.array(mcin['longitude'])
nom = np.array(mc_in['name'])

for i in range(len(lat)):
    folium.Marker([lat[i],lon[i]],popup=nom[i],icon=folium.Icon(color='red')).add_to(m)

lat2 = np.array(mcout['latitude'])
lon2 = np.array(mcout['longitude'])
nom2 = np.array(mc_out['name'])

for i in range(len(lat2)):
    folium.Marker([lat2[i],lon2[i]],popup=nom2[i],icon=folium.Icon(color='black')).add_to(m)   

 
    
m.save('Mc_map.html') 


# In[39]:


Mc_id = mc['business_id']
#Mc_id.to_csv('Mc_id.csv')


# In[40]:


Mcin_id = mc_in['business_id']
Mcout_id = mc_out['business_id']
#Mcin_id.to_csv('Mcin_id.csv')


# In[41]:


mc_in.head(3)


# In[42]:


bool = mc['hours.Friday']=='0:0-0:0' 
mc_247 = mc[bool.values==True]
mc_247.head(3)


# In[ ]:





# In[43]:


map = Basemap(projection='stere',lat_0=90,lon_0=-105,            llcrnrlat=23.41 ,urcrnrlat=55.44,            llcrnrlon=-118.67,urcrnrlon=-44.52,            rsphere=6371200.,resolution='l',area_thresh=10000)
map.drawmapboundary()
#map.drawmapboundary(fill_color = 'skyblue')   # 绘制边界
#map.fillcontinents(color = 'coral') # 填充大陆，发现填充之后无法显示散点图，应该是被覆盖了
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
#map.drawcounties()      # 绘制县
parallels = np.arange(0.,90,10.) 
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线
meridians = np.arange(-110.,-60.,10.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线
lat = np.array(mc_247['latitude'])
lon = np.array(mc_247['longitude'])
x,y = map(lon,lat)
map.scatter(x,y,color = 'red', marker = 'o')    
plt.title('McDonald\'s in North America')
plt.show()


# In[44]:


br = pd.read_csv( '/Users/zzz/Desktop/STAT628/Module 2/br.csv',encoding='latin-1')
br.head(3)


# In[45]:


bool = br['review_index'].isnull()
fbr = br[bool.values==False]
fbr.head(3)
r_index = fbr['review_index']
r_index = r_index.astype(int)


# In[46]:


id = fbr['business_id']
id = id.unique()
id = list(id)

data_file = '/Users/zzz/Desktop/STAT628/Module 2/Data/review_train.json'

r_sample = []
with open(data_file, 'r') as f:
    r_sample.append(f.readlines())

r_sample = r_sample[0]
review = []
for i in range(0,len(r_sample)):
    r_review = json.loads(r_sample[i])
    if r_review['business_id'] in id:
        review.append(r_review)review[0]['business_id']fbr.info()business_id = []
text = []
stars = []for i in range(0,1986):
    business_id.append(review[i]['business_id'])
    text.append(review[i]['text'])
    stars.append(review[i]['stars'])mc_r = pd.DataFrame(business_id)
mc_r.insert(1,'text',text)
mc_r.insert(2,'stars',stars)
#mc_r.to_csv("mc_r.csv")mc_r = pd.read_csv( '/Users/zzz/Desktop/STAT628/Module 2/mc_r.csv',encoding='latin-1')
mc_r.head(3)smc = mc.iloc[:,lambda df:[1,57]]
smc.head(6)
#smc.to_csv("smc.csv")
smc = pd.read_csv( '/Users/zzz/Desktop/STAT628/Module 2/smc.csv',encoding='latin-1')smc.info()mc_r.info()MC = pd.merge(smc,mc_r)
MC.to_csv("MC.csv")
# In[47]:


map = Basemap(projection='stere',lat_0=90,lon_0=-105,            llcrnrlat=23.41 ,urcrnrlat=55.44,            llcrnrlon=-118.67,urcrnrlon=-44.52,            rsphere=6371200.,resolution='l',area_thresh=10000)
map.drawmapboundary()
map.drawstates()        # 绘制州
map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
#map.drawcounties()      # 绘制县
parallels = np.arange(0.,90,10.) 
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线
meridians = np.arange(-110.,-60.,10.)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线
lat = np.array(mc['latitude'])
lon = np.array(mc['longitude'])
x,y = map(lon,lat)
map.scatter(x,y,color = 'red', marker = 'o')
x1,y1 = map(np.array(mc_247['latitude']),np.array(mc_247['longitude']))
map.scatter(x1,y1,color = 'black', marker = 'o')
plt.title('McDonald\'s in North America')
plt.show()


# In[48]:


mcp = pd.DataFrame(mc.iloc[:,lambda df:[6,7]] ,dtype=np.float)
mcp.head(3)


# In[49]:


mc24 = pd.DataFrame(mc_247.iloc[:,lambda df:[6,7]] ,dtype=np.float)
mc24.head(3)


# In[50]:


from folium import plugins
import folium
import os

m = folium.Map([40, -100], zoom_start=5)  #中心区域的确定

lat = np.array(mcp['latitude'])
lon = np.array(mcp['longitude'])
nom = np.array(mc['name'])

for i in range(len(lat)):
    folium.Marker([lat[i],lon[i]],popup=nom[i],icon=folium.Icon(color='red')).add_to(m)

lat2 = np.array(mc24['latitude'])
lon2 = np.array(mc24['longitude'])
nom2 = np.array(mc_247['name'])

for i in range(len(lat2)):
    folium.Marker([lat2[i],lon2[i]],popup=nom2[i],icon=folium.Icon(color='black')).add_to(m)   
    
m.save('Mc_map2.html') 


# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


#mc.info()


# In[52]:


set([i.split(',', 1)[0] for i in mc['categories']])


# In[ ]:





# In[ ]:





# In[53]:


mc1 = pd.read_csv('/Users/zzz/Dropbox/未命名文件夹/data/circle and store/Mc.csv',encoding='latin-1')


# In[54]:


mc1['length'] = mc1['text'].apply(len)
mc1.head()


# In[ ]:





# In[ ]:





# In[55]:


mc1['length'].mean()


# In[56]:


star = np.array([1., 2., 3., 4., 5.])
c = [sum(mc1['stars']==1),sum(mc1['stars']==2),sum(mc1['stars']==3),sum(mc1['stars']==4),sum(mc1['stars']==5)]
fig = plt.figure()
plt.bar(star,c)
plt.xlabel("Stars")
plt.ylabel("Numbers")
#plt.title("Dist of stars")
plt.show()


# In[57]:


#mc1.sort_values('business_id').head(3)


# In[58]:


graph = sns.FacetGrid(data=mc1,col='stars')
graph.map(plt.hist,'length',bins=50,color='blue')


# In[59]:


bool = mc1['circle'] ==1
mcin = mc1[bool.values == True]

mcin = pd.read_csv('/Users/zzz/Dropbox/未命名文件夹/data/mcin.csv',encoding='latin-1')
mcin.loc[:,'length'] = mcin['text'].apply(len)
mcin.head()


# In[60]:


mcin['length'].mean()


# In[61]:


star = np.array([1., 2., 3., 4., 5.])
c = [sum(mcin['stars']==1),sum(mcin['stars']==2),sum(mcin['stars']==3),sum(mcin['stars']==4),sum(mcin['stars']==5)]
fig = plt.figure()
plt.bar(star,c)
plt.xlabel("Stars")
plt.ylabel("Numbers")
#plt.title("Dist of stars")
plt.show()


# In[62]:


graph = sns.FacetGrid(data=mcin,col='stars')
graph.map(plt.hist,'',bins=50,color='blue')


# In[63]:


bool = mc1['circle'] ==0
mcout = mc1[bool.values == True]
mcout['length'] = mcout['text'].apply(len)
mcout.head()
#mcout.to_csv('mcout.csv') 


# In[64]:


mcout['length'].mean()


# In[65]:


star = np.array([1., 2., 3., 4., 5.])
c = [sum(mcout['stars']==1),sum(mcout['stars']==2),sum(mcout['stars']==3),sum(mcout['stars']==4),sum(mcout['stars']==5)]
fig = plt.figure()
plt.bar(star,c)
plt.xlabel("Stars")
plt.ylabel("Numbers")
#plt.title("Dist of stars")
plt.show()

import re
from langdetect import detect
def not_lang(text):
    text = re.sub('(?::|;|=)(?:-)?(?:\)|\(|D|P)','',text)
    if re.sub('[\W]+','',text) == '':
        return True
    else:
        return False
temp=mc1[mc1['text'].apply(not_lang)].index.values
mc1.loc[temp,'lang_type'] = 'en'
from langdetect import detect
for i in range(mc1.shape[0]):
    if i in temp:
        continue
    else:
        mc1.loc[i,'lang_type'] = detect(mc1['text'][i])
#translate the language
mc1['lang_type'].describe()

from googletrans import Translator
translator = Translator()
#data_df['lang_type'].describe(include=['O'])
c='你好'
c.encode('utf8')
translator.translate(c).text
#from translate import Translator
#translator= Translator(to_lang="German")
#translator.translate('你好')
# In[66]:


import re

mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
mc1['text']=mc1['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))


# In[ ]:




#!!!!!!!!!!!!!!!!!!!!!



# In[ ]:





# In[ ]:





# In[67]:


data_dict=mcin
data_dict.loc[:,'text'] = data_dict.loc[:,'text'].apply(lambda x: x.lower())

#remove the punctuation
#data_dict['text'] = data_dict['text'].apply(lambda x: ''.join([c for c in x if c not in punctuation]))


# In[68]:


import re

mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
mcin.loc[:,'text']=mcin['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))


# In[69]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import nltk 
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english')) 

from nltk import *
data_dict.loc[:,'NN'] =None
data_dict.loc[:,'JJ']=None
data_dict.loc[:,'RB']=None

import numpy as np
def detect(text):
    NN = []
    JJ = []
    RB = []
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    i = 0
    for word, tag in temp:
        if word in stop_words:
            continue
        if re.match('JJ[*]?', tag) != None:
            JJ.append(word)
        if re.match('NN[*]?', tag) != None:
            NN.append(word)
        if re.match('RB[*]?', tag) != None:
            RB.append(word)
    return list([NN, JJ, RB])

temp = pd.DataFrame(list(data_dict['text'].apply(detect)))
data_dict['NN'], data_dict['JJ'], data_dict['RB'] = temp[:][0], temp[:][1], temp[:][2]


# In[70]:


data_dict.head()


# In[71]:


star1=data_dict[data_dict['stars']==1]
star2=data_dict[data_dict['stars']==2]
star3=data_dict[data_dict['stars']==3]
star4=data_dict[data_dict['stars']==4]
star5=data_dict[data_dict['stars']==5]


# In[72]:


NN = []
for item in data_dict['NN']:
    NN += item
#count the words
from collections import Counter

words=NN
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
print('Unique words: ', len((vocab_to_int_n)))
counts.most_common(20)


# In[73]:


JJ = []
for item in data_dict['JJ']:
    JJ += item
#count the words
from collections import Counter

words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
print('Unique words: ', len((vocab_to_int_j)))
counts.most_common(20)


# In[74]:


#####################
RB = []
for item in data_dict['RB']:
    RB += item
#count the words
from collections import Counter

words=RB

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_r = {word: ii for ii, word in enumerate(vocab, 1)}
#常见R
print('Unique words: ', len((vocab_to_int_r)))
counts.most_common(20)

reviews_ints_r = []
reviews_ints_r.append([vocab_to_int_r[word] for word in RB])


# In[75]:


plt.style.use('ggplot')
tt = ' '.join(NN)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
#plt.title('Reviews',size=20)
plt.show()


# In[76]:


plt.style.use('ggplot')
tt = ' '.join(JJ)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
#plt.title('Reviews',size=20)
plt.show()


# In[77]:


mc1 = pd.read_csv('/Users/zzz/Dropbox/未命名文件夹/data/circle and store/Mc.csv',encoding='latin-1')
mc1['length'] = mc1['text'].apply(len)
mc1.head()


# In[78]:


mc1.info()


# In[79]:


mc1 = mc1.sort_values('business_id')
mc1.head(3)


# In[80]:


mc1['stars'].mean()


# In[81]:


m = mc1.groupby('business_id')['stars'].mean()
#m


# In[82]:


num = mc1.groupby('business_id')['stars'].count()
#num


# In[83]:


a = mc1['business_id'].unique()
business_id = []
stars=[]
Num=[]
for i in a:    
    business_id.append(i)
    stars.append(m[i])
    Num.append(num[i])
    #print(i,m[i],num[i])
    
df = pd.DataFrame({'business_id':business_id,'avgstar':stars,'num':Num})
df.head(3)


# In[84]:


df5 = df[df['num']<=5]
df5.head(3) #147


# In[85]:


df4 = df[df['num']>=5]
df4.head(3) #558


# In[86]:


star = np.array([2., 3., 4., 5.])
s2 = sum(df4['avgstar']<=2)
s3 = sum(df4['avgstar']<=3)
s4 = sum(df4['avgstar']<=4)
s5 =sum(df4['avgstar']<=5)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 30,
         }

c = [s2,s3-s2,s4-s3,s5-s4] #[322, 203, 32, 1]
#fig = plt.figure()
figsize = 14,8
figure, ax = plt.subplots(figsize=figsize)

plt.tick_params(labelsize=23)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]


plt.bar(star,c)
plt.xlabel("avg_star", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of stars", font2)
plt.xlim([1,5])

plt.show()


# In[87]:


df4.head(3)


# In[88]:


new_Mc = pd.merge(mc1,df4)
new_Mc.head(3)


# In[89]:


l_mc = new_Mc[new_Mc['avgstar']<=2]
#l_mc.to_csv("l_mc.csv")
l_mc = pd.read_csv('l_mc.csv',encoding='latin-1')


# In[90]:


l_mc.shape[0]


# In[91]:


h_mc = new_Mc[new_Mc['avgstar']>2]
h_mc.to_csv("h_mc.csv")
h_mc = pd.read_csv('h_mc.csv',encoding='latin-1')


# In[92]:


h_mc.shape[0]


# In[104]:


NN1 = NN
words=NN1
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
#print('Unique words: ', len((vocab_to_int_n)))
#counts.most_common(20)


# In[105]:


'''
a = vocab
nouns = []
freq=[]
Num=[]
l = counts.sum
for i in a:    
    nouns.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_n)))   
    
#l_nouns = pd.DataFrame({'noun':nouns,'num':Num,'freq':freq})
#l_nouns.to_csv("l_nouns.csv")

'''
l_nouns = pd.read_csv("l_nouns.csv")
fre = l_nouns['nums']/7082
l_nouns['freqs'] = fre
l_nouns.head(3)


# In[106]:


JJ1 = JJ
words=JJ1
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
#print('Unique words: ', len((vocab_to_int_j)))
#counts.most_common(20)


# In[107]:


a = vocab
adjs = []
freq=[]
Num=[]
for i in a:    
    adjs.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_j)))   
    
#l_adjs = pd.DataFrame({'adj':adjs,'num':Num,'freq':freq})
#l_adjs.to_csv("l_adjs.csv")
l_adjs = pd.read_csv("l_adjs.csv")
fre = l_adjs['nums']/7082
l_adjs['freqs'] = fre
l_adjs.head(3)


# In[108]:


#NN2 = NN
words=NN
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
#print('Unique words: ', len((vocab_to_int_n)))
#counts.most_common(20)


# In[109]:


a = vocab
nouns = []
freq=[]
Num=[]
for i in a:    
    nouns.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_n)))   
    
#h_nouns = pd.DataFrame({'noun':nouns,'num':Num,'freq':freq})
#h_nouns.to_csv("h_nouns.csv")
h_nouns = pd.read_csv("h_nouns.csv")
fre = h_nouns['num']/4519
h_nouns['freq'] = fre
h_nouns.head(3)

#JJ2 = JJ
words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
#print('Unique words: ', len((vocab_to_int_j)))
#counts.most_common(20)
# In[110]:


a = vocab
adjs = []
freq=[]
Num=[]
for i in a:    
    adjs.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_j)))   
    
#h_adjs = pd.DataFrame({'adj':adjs,'num':Num,'freq':freq})
#h_adjs.to_csv("h_adjs.csv")
h_adjs = pd.read_csv("h_adjs.csv")
fre = h_adjs['num']/4519
h_adjs['freq'] = fre
h_adjs.head(3)


# In[ ]:





# In[111]:


l_nouns.head()


# In[112]:


h_nouns.head()


# In[113]:


new = pd.merge(l_nouns,h_nouns, on = 'noun')
new['FREQ'] = new['freq']-new['freqs'] #freqs--> l_nouns
new = new.iloc[(-new['FREQ'].abs()).argsort()]
new.head()
new.to_csv("new.csv")
new = pd.read_csv("new.csv")
new.head()


# In[114]:


(new['FREQ']<0).sum()


# In[115]:


y = new['FREQ'].head(20)
x = new['noun'].head(20)


# In[116]:


figsize = 50,28.5
figure, ax = plt.subplots(figsize=figsize)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 100,
         }

plt.tick_params(labelsize=100)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.barh(x,y)
plt.xlabel("Nouns", font2)
plt.ylabel("Differences of frequences", font2)
plt.title("Top 20 of Nouns", font2)
#plt.xlim([-2,20])
#plt.xticks(rotation=60)

plt.show()


# In[117]:


l_adjs.head()


# In[118]:


h_adjs.head()


# In[119]:


old = pd.merge(l_adjs,h_adjs, on = 'adj')
old['FREQ'] = old['freq']-old['freqs'] #freqs--> l_nouns
old = old.iloc[(-old['FREQ'].abs()).argsort()]
old.head()
#old.to_csv("old.csv")
#old = pd.read_csv("old.csv")
old.head()


# In[120]:


y = old['FREQ'].head(20)
x = old['adj'].head(20)


# In[121]:


figsize = 50,28.5
figure, ax = plt.subplots(figsize=figsize)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 100,
         }
plt.tick_params(labelsize=100)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.barh(x,y)
plt.xlabel("Adjs", font2)
plt.ylabel("Differences of frequences", font2)
plt.title("Top 20 of Adjs", font2)
#plt.xlim([-1,20])
#plt.xticks(rotation=45)
plt.show()


# In[93]:


#new_mc.head(3)


# In[94]:


import re

l_mc.loc[:,'text']=l_mc['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
l_mc['text']=l_mc['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))


# In[95]:


h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
h_mc['text']=h_mc['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))


# In[96]:


data_dict=l_mc


# In[97]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import nltk 
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english')) 

from nltk import *
data_dict.loc[:,'NN'] =None
data_dict.loc[:,'JJ']=None
data_dict.loc[:,'RB']=None


import numpy as np
def detect(text):
    NN = []
    JJ = []
    RB = []
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    i = 0
    for word, tag in temp:
        if word in stop_words:
            continue
        if re.match('JJ[*]?', tag) != None:
            JJ.append(word)
        if re.match('NN[*]?', tag) != None:
            NN.append(word)
        if re.match('RB[*]?', tag) != None:
            RB.append(word)
    return list([NN, JJ, RB])

temp = pd.DataFrame(list(data_dict['text'].apply(detect)))
data_dict['NN'], data_dict['JJ'], data_dict['RB'] = temp[:][0], temp[:][1], temp[:][2]

star1=data_dict[data_dict['stars']==1]
star2=data_dict[data_dict['stars']==2]
star3=data_dict[data_dict['stars']==3]
star4=data_dict[data_dict['stars']==4]
star5=data_dict[data_dict['stars']==5]
# In[98]:


#data_dict['NN'].head()


# In[99]:


NN = []

for item in data_dict['NN']:
    NN += item
#count the words
from collections import Counter

#count the words
words=NN

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
print('Unique words: ', len((vocab_to_int_n)))
counts.most_common(20)


# In[100]:


JJ = []
for item in data_dict['JJ']:
    JJ += item
#count the words
from collections import Counter

words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
print('Unique words: ', len((vocab_to_int_j)))
counts.most_common(20)


# In[101]:


#####################
RB = []
for item in data_dict['RB']:
    RB += item
#count the words
from collections import Counter

words=RB

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_r = {word: ii for ii, word in enumerate(vocab, 1)}
#常见R
print('Unique words: ', len((vocab_to_int_r)))
counts.most_common(20)

reviews_ints_r = []
reviews_ints_r.append([vocab_to_int_r[word] for word in RB])


# In[102]:


plt.style.use('ggplot')
tt = ' '.join(NN)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
#plt.title('Reviews',size=20)
plt.show()


# In[103]:


plt.style.use('ggplot')
tt = ' '.join(JJ)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
#plt.title('Reviews',size=20)
plt.show()


# In[ ]:





# In[104]:


NN1 = NN
words=NN1
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
#print('Unique words: ', len((vocab_to_int_n)))
#counts.most_common(20)


# In[105]:


'''
a = vocab
nouns = []
freq=[]
Num=[]
l = counts.sum
for i in a:    
    nouns.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_n)))   
    
#l_nouns = pd.DataFrame({'noun':nouns,'num':Num,'freq':freq})
#l_nouns.to_csv("l_nouns.csv")

'''
l_nouns = pd.read_csv("l_nouns.csv")
fre = l_nouns['nums']/7082
l_nouns['freqs'] = fre
l_nouns.head(3)


# In[106]:


JJ1 = JJ
words=JJ1
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
#print('Unique words: ', len((vocab_to_int_j)))
#counts.most_common(20)


# In[107]:


a = vocab
adjs = []
freq=[]
Num=[]
for i in a:    
    adjs.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_j)))   
    
#l_adjs = pd.DataFrame({'adj':adjs,'num':Num,'freq':freq})
#l_adjs.to_csv("l_adjs.csv")
l_adjs = pd.read_csv("l_adjs.csv")
fre = l_adjs['nums']/7082
l_adjs['freqs'] = fre
l_adjs.head(3)


# In[108]:


#NN2 = NN
words=NN
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
#print('Unique words: ', len((vocab_to_int_n)))
#counts.most_common(20)


# In[109]:


a = vocab
nouns = []
freq=[]
Num=[]
for i in a:    
    nouns.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_n)))   
    
#h_nouns = pd.DataFrame({'noun':nouns,'num':Num,'freq':freq})
#h_nouns.to_csv("h_nouns.csv")
h_nouns = pd.read_csv("h_nouns.csv")
fre = h_nouns['num']/4519
h_nouns['freq'] = fre
h_nouns.head(3)

#JJ2 = JJ
words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
#print('Unique words: ', len((vocab_to_int_j)))
#counts.most_common(20)
# In[110]:


a = vocab
adjs = []
freq=[]
Num=[]
for i in a:    
    adjs.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/len((vocab_to_int_j)))   
    
#h_adjs = pd.DataFrame({'adj':adjs,'num':Num,'freq':freq})
#h_adjs.to_csv("h_adjs.csv")
h_adjs = pd.read_csv("h_adjs.csv")
fre = h_adjs['num']/4519
h_adjs['freq'] = fre
h_adjs.head(3)


# In[ ]:





# In[111]:


l_nouns.head()


# In[112]:


h_nouns.head()


# In[113]:


new = pd.merge(l_nouns,h_nouns, on = 'noun')
new['FREQ'] = new['freq']-new['freqs'] #freqs--> l_nouns
new = new.iloc[(-new['FREQ'].abs()).argsort()]
new.head()
new.to_csv("new.csv")
new = pd.read_csv("new.csv")
new.head()


# In[114]:


(new['FREQ']<0).sum()


# In[115]:


y = new['FREQ'].head(20)
x = new['noun'].head(20)


# In[116]:


figsize = 50,28.5
figure, ax = plt.subplots(figsize=figsize)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 100,
         }

plt.tick_params(labelsize=100)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.barh(x,y)
plt.xlabel("Nouns", font2)
plt.ylabel("Differences of frequences", font2)
plt.title("Top 20 of Nouns", font2)
#plt.xlim([-2,20])
#plt.xticks(rotation=60)

plt.show()


# In[117]:


l_adjs.head()


# In[118]:


h_adjs.head()


# In[119]:


old = pd.merge(l_adjs,h_adjs, on = 'adj')
old['FREQ'] = old['freq']-old['freqs'] #freqs--> l_nouns
old = old.iloc[(-old['FREQ'].abs()).argsort()]
old.head()
#old.to_csv("old.csv")
#old = pd.read_csv("old.csv")
old.head()


# In[120]:


y = old['FREQ'].head(20)
x = old['adj'].head(20)


# In[121]:


figsize = 50,28.5
figure, ax = plt.subplots(figsize=figsize)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 100,
         }
plt.tick_params(labelsize=100)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.barh(x,y)
plt.xlabel("Adjs", font2)
plt.ylabel("Differences of frequences", font2)
plt.title("Top 20 of Adjs", font2)
#plt.xlim([-1,20])
#plt.xticks(rotation=45)
plt.show()

mc.info()
# In[122]:


a = mc_247.iloc[:,lambda df:[2,3,4,5,6,7,8,9,10,11,13,16,18,19,20,22,23,24,26,27,40,49,50,51,52,53,54,55,57]]
a.head()


# In[123]:


a.info()


# In[124]:


font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 50,
         }

star = np.array(['1', '2', '3', '4'])
c = [sum(mc['attributes.RestaurantsPriceRange2']=='1'),
     sum(mc['attributes.RestaurantsPriceRange2']=='2'),
     sum(mc['attributes.RestaurantsPriceRange2']=='3'),
     sum(mc['attributes.RestaurantsPriceRange2']=='4')]
fig = plt.figure()

plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.bar(star,c)
plt.xlabel("Price range", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of price", font2)
plt.show()


# In[125]:


font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 50,
         }
star = np.array(['TRUE', 'FALSE'])
c = [sum(mc['attributes.GoodForKids']=='TRUE')+ sum(mc['attributes.GoodForKids']=='1'),
     sum(mc['attributes.GoodForKids']=='FALSE') + sum(mc['attributes.GoodForKids']=='0')]
fig = plt.figure()
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.bar(star,c)
plt.xlabel("GoodForKids", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of GoodForKids", font2)
plt.show()


# In[126]:


KID = mc[mc['attributes.GoodForKids']=='FALSE']
KID.head(3)
#mc['circle'].unique()
#sum(mc['circle']=='0')+ sum(mc['circle']=='1')


# In[127]:


star = np.array(["out", "in"])
c = [sum(KID['circle']=='0'),
     sum(KID['circle']=='1')]
fig = plt.figure()
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.bar(star,c)
plt.xlabel("In or Out business districts", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of not GoodForKids", font2)
plt.show()


# In[128]:


star = np.array(["u'free'", "'free'", "'no'", "'paid'", "u'no'", "u'paid'"])
c = [sum(mc['attributes.WiFi']=="u'free'"),
     sum(mc['attributes.WiFi']=="'free'"),
     sum(mc['attributes.WiFi']=="'no'"),
     sum(mc['attributes.WiFi']=="'paid'"),
     sum(mc['attributes.WiFi']=="u'no'"),
     sum(mc['attributes.WiFi']=="u'paid'")]
fig = plt.figure()
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.barh(star,c)
plt.xlabel("WIFI", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of WIFI", font2)
plt.show()


# In[129]:


star = np.array(["u'average'", "'average'", "u'loud'", "u'very_loud'","'quiet'", "u'quiet'", "'loud'", "'very_loud'"])
c = [sum(mc['attributes.NoiseLevel']=="u'average'"),
     sum(mc['attributes.NoiseLevel']=="'average'"),
     sum(mc['attributes.NoiseLevel']=="u'loud'"),
     sum(mc['attributes.NoiseLevel']=="u'very_loud'"),
     sum(mc['attributes.NoiseLevel']=="'quiet'"),
     sum(mc['attributes.NoiseLevel']=="u'quiet'"),
     sum(mc['attributes.NoiseLevel']=="'loud'"),
     sum(mc['attributes.NoiseLevel']=="'very_loud'")]
fig = plt.figure()
plt.tick_params(labelsize=30)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.barh(star,c)
plt.xlabel("NoiseLevel", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of NoiseLevel",font2)
plt.show()


# In[130]:


sum(mc['attributes.GoodForMeal'].str.contains('.latenight\': True.') == True)


# In[131]:


star = np.array(["latenight","dinner", "dessert", "lunch","brunch", "breakfast"])
c = [sum(mc['attributes.GoodForMeal'].str.contains('.latenight\': True.') == True),
     sum(mc['attributes.GoodForMeal'].str.contains('.dinner\': True.') == True),
     sum(mc['attributes.GoodForMeal'].str.contains('.dessert\': True.') == True),
     sum(mc['attributes.GoodForMeal'].str.contains('.lunch\': True.') == True),
     sum(mc['attributes.GoodForMeal'].str.contains('.brunch\': True.') == True),
     sum(mc['attributes.GoodForMeal'].str.contains('.breakfast\': True.') == True)]
fig = plt.figure()
plt.bar(star,c)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.bar(star,c)
plt.tick_params(labelsize=30)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("GoodForMeal",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of GoodForMeal",font2)
plt.show()


# In[132]:


star = np.array(["casual","divey", "touristy"])
c = [sum(mc['attributes.Ambience'].str.contains('.casual\': True.') == True),
     sum(mc['attributes.Ambience'].str.contains('.divey\': True.') == True),
     sum(mc['attributes.Ambience'].str.contains('.touristy\': True.') == True)]
fig = plt.figure()
plt.bar(star,c)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.bar(star,c)
plt.tick_params(labelsize=30)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("Ambience",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of Ambience",font2)
plt.show()

mc['attributes.Ambience'].unique()
# In[133]:


star = np.array(['24/7', 'not 24/7'])
c = [sum(mc['hours.Monday']=='0:0-0:0'),
     mc.shape[0] - sum(mc['hours.Monday'] == None) - sum(mc['hours.Monday']=='0:0-0:0')]
fig = plt.figure()
plt.bar(star,c)
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("hours.Monday",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of hours.Monday",font2)
plt.show()


# In[134]:


star = np.array(['24/7', 'not 24/7'])
c = [sum(mc['hours.Sunday']=='0:0-0:0'),
     mc.shape[0] - sum(mc['hours.Sunday']=='0:0-0:0')]
fig = plt.figure()
plt.bar(star,c)
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("hours.Sunday",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of hours.Sunday",font2)
plt.show()


# In[135]:


star = np.array(['TRUE', 'FALSE'])
c = [sum(mc['attributes.OutdoorSeating']=='TRUE'),
     sum(mc['attributes.OutdoorSeating']=='FALSE')]
fig = plt.figure()
plt.bar(star,c)
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("OutdoorSeating",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of OutdoorSeating",font2)
plt.show()


# In[136]:


star = np.array(['TRUE', 'FALSE'])
c = [sum(mc['attributes.DriveThru']=='TRUE')+sum(mc['attributes.DriveThru']=='1'),
     sum(mc['attributes.DriveThru']=='FALSE')+sum(mc['attributes.DriveThru']=='0')]
fig = plt.figure()
plt.bar(star,c)
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("DriveThru",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of DriveThru",font2)
plt.show()


# In[137]:


star = np.array(['TRUE', 'FALSE'])
c = [sum(mc['attributes.RestaurantsReservations']=='TRUE'),
     sum(mc['attributes.RestaurantsReservations']=='FALSE')+sum(mc['attributes.RestaurantsReservations']=='0')]
fig = plt.figure()
plt.bar(star,c)
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("RestaurantsReservations",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of RestaurantsReservations",font2)
plt.show()


# In[138]:


star = np.array(['TRUE', 'FALSE'])
c = [sum(mc['attributes.HasTV']=='TRUE'),
     sum(mc['attributes.HasTV']=='FALSE')]
fig = plt.figure()
plt.bar(star,c)
plt.tick_params(labelsize=50)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.xlabel("HasTV",font2)
plt.ylabel("Numbers",font2)
plt.title("Dist of HasTV",font2)
plt.show()


# In[ ]:





# In[3]:


f = pd.read_csv( '/Users/zzz/Dropbox/未命名文件夹/data/restaurant/all.csv',encoding = 'latin-1')

f.info()
# In[4]:


bool = f['name'].str.contains('McDonald.') 
mc = f[bool.values==True]
mc.head(6)


# In[5]:


pwd

name = f['name'].unique()
n = 0
for i in name:
    n = (f['name']==i).sum
    print(i,n)
# In[6]:


from dfply import *


# In[7]:


top20 = pd.read_csv( '/Users/zzz/Dropbox/未命名文件夹/data/top20.csv',encoding = 'latin-1',index_col=0)
top20


# In[8]:


bool = f['name'].str.contains('.ubwa.') 
sb = f[bool.values==True]
sb.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/subway.csv')
sb.head(3)


# In[9]:


bool = f['name'].str.contains('.izza Hu.') 
pz = f[bool.values==True]
pz.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/pizzahut.csv')
pz.head(3)


# In[10]:


bool = f['name'].str.contains('.aco Bel.') 
tb = f[bool.values==True]
tb.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/tacobell.csv')
tb.head(3)
#tb['name'].unique()


# In[11]:


bool = f['name'].str.contains('.urger Kin.') 
bk = f[bool.values==True]
bk.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/burgerking.csv')
bk.head(3)
#bk['name'].unique()


# In[12]:


bool = f['name']=='Wendy\'s'
wd = f[bool.values==True]
#wd.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/wendys.csv')
wd = pd.read_csv( '/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/wendys.csv',encoding = 'latin-1')
wd.head(3)
#wd['name'].unique()

bool = f['name']=='Wendys'
wd2 = f[bool.values==True]
#wd2.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/wendys2.csv')
wd2.head(3)
wd['name'].unique()
# In[13]:


bool = f['name'].str.contains('.tarbuck.') 
starb = f[bool.values==True]
#starb.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/starbucks.csv')
starb.head(3)
#starb['name'].unique()


# In[14]:


bool = f['name'].str.contains('.omino\'s Pizz.') 
dp = f[bool.values==True]
#dp.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/dominospizza.csv')
dp.head(3)
#dp['name'].unique()


# In[15]:


bool = f['name'].str.contains('KFC') 
kfc = f[bool.values==True]
#kfc.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/KFC.csv')
kfc.head(3)
#kfc['name'].unique()


# In[16]:


bool = f['name'].str.contains('.hipotle Mexican Gril.') 
cmg = f[bool.values==True]
#cmg.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Chipotle_Mexican_Grill.csv')
cmg.head(3)
#cmg['name'].unique()


# In[17]:


bool = f['name'].str.contains('.im Horto.') 
th = f[bool.values==True]
#th.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Tim_Hortons.csv')
th.head(3)
#th['name'].unique()


# In[18]:


bool = f['name'].str.contains('.immy Joh.') 
jj = f[bool.values==True]
#jj.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Jimmy_Johns.csv')
jj.head(3)
#jj['name'].unique()


# In[19]:


bool = f['name'].str.contains('.apa John\'s Pizz.') 
pj = f[bool.values==True]
#pj.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Papa_Johns_Pizza.csv')
pj.head(3)
#pj['name'].unique()


# In[20]:


bool = f['name'].str.contains('.anera Brea.') 
pb = f[bool.values==True]
#pb.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Panera_Bread.csv')
pb.head(3)
#pb['name'].unique()


# In[21]:


bool = f['name'].str.contains('.anda Expres.') 
pe = f[bool.values==True]
pe.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Panda Express.csv')
pe.head(3)
#pe['name'].unique()


# In[22]:


bool = f['name'].str.contains('.opeyes Louisiana Kitche.') 
plk = f[bool.values==True]
#plk.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Popeyes_Louisiana_Kitchen.csv')
plk.head(3)
#plk['name'].unique()


# In[23]:


bool = f['name'].str.contains('.airy Quee.') 
dq = f[bool.values==True]
#dq.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Dairy_Queen.csv')
dq.head(3)
#dq['name'].unique()


# In[24]:


bool = f['name'].str.contains('Arby\'s.') 
ar = f[bool.values==True]
#ar.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Arbys.csv')
ar.head(3)
#ar['name'].unique()


# In[25]:


bool = f['name'].str.contains('Denny.') 
den = f[bool.values==True]
#den.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Dennys.csv')
den.head(3)
#den['name'].unique()


# In[26]:


bool = f['name'].str.contains('.ittle Caesars.') 
lcp = f[bool.values==True]
#lcp.to_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/Little_Caesars_Pizza.csv')
lcp.head(3)
#lcp['name'].unique()

import pandas as pd
import os
Folder_Path = r'/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/'          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path =  r'/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/'       #拼接后要保存的文件路径
SaveFile_Name = r'all.csv'              #合并后要保存的文件名



#修改当前工作目录
os.chdir(Folder_Path)
#将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()
 
#读取第一个CSV文件并包含表头
df = pd.read_csv(Folder_Path + file_list[0],index_col=0)   #编码默认UTF-8，若乱码自行更改
 
#将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path+ SaveFile_Name,encoding="utf_8_sig",index=False)
 
#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path +  file_list[i],index_col=0)
    df.to_csv(SaveFile_Path+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')
# In[27]:


all1 = pd.read_csv( '/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/all.csv',encoding = 'latin-1',index_col=0)
all1.info()


# In[28]:


top20['n'].sum()


# In[29]:


all1.head(3)


# In[30]:


all1 = pd.read_csv( '/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/all.csv',encoding = 'latin-1',index_col=0)
all1.info()


# In[38]:


r_sample1 = r_sample[0]
#r_sample1


# In[37]:


r_sample1[1]


# In[31]:


top20


# In[32]:


sb = pd.read_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/subway.csv',encoding = 'latin-1',index_col=0)
sb.info()


# In[104]:


bid = sb['business_id'].unique()


# In[48]:


import json
data_file = '/Users/zzz/Desktop/STAT628/Module 2/Data/review_train.json'

r_sample = []
with open(data_file, 'r') as f:
    r_sample.append(f.readlines())


# In[49]:


r_sample1 = r_sample[0]
review = []

for i in range(0,len(r_sample1)):
    r_review = json.loads(r_sample1[i])
    if r_review['business_id'] in bid:
        review.append(r_review)


# In[50]:


review[0]['business_id']


# In[67]:


business_id = []
text = []
stars = []
name = []


# In[68]:


for i in range(0,1986):
    business_id.append(review[i]['business_id'])
    text.append(review[i]['text'])
    stars.append(review[i]['stars'])


# In[81]:


sb_r = pd.DataFrame(business_id)
sb_r.insert(1,'text',text)
sb_r.insert(2,'stars',stars)
sb_r.columns = ['business_id', 'text','stars']
#sb_r.to_csv("/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/subway_r.csv")
sb_r.head(3)


# In[82]:


sb_r.info()


# In[113]:


ssb = sb.iloc[:,lambda df:[1,3,4,57]]
ssb.head(3)


# In[114]:


SB = pd.merge(ssb,sb_r)
SB.to_csv("/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/subway_r.csv")
SB.head(3)


# In[115]:


SB.shape[0]


# In[116]:


import re

SB.loc[:,'text']=SB['text'].apply(lambda sen: re.sub(r"can\'t", "can not", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"cannot", "can not ", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"what\'s", "what is", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"\'ve ", " have ", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"n\'t", " not ", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"i\'m", "i am ", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"\'re", " are ", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"\'d", " would ", sen))
SB['text']=SB['text'].apply(lambda sen: re.sub(r"\'ll", " will ", sen))


# In[118]:


data_dict=SB

star1=data_dict[data_dict['stars']==1]
star2=data_dict[data_dict['stars']==2]
star3=data_dict[data_dict['stars']==3]
star4=data_dict[data_dict['stars']==4]
star5=data_dict[data_dict['stars']==5]
# In[119]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import nltk 
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english')) 

from nltk import *
data_dict.loc[:,'NN'] =None
data_dict.loc[:,'JJ']=None
data_dict.loc[:,'RB']=None


import numpy as np
def detect(text):
    NN = []
    JJ = []
    RB = []
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    i = 0
    for word, tag in temp:
        if word in stop_words:
            continue
        if re.match('JJ[*]?', tag) != None:
            JJ.append(word)
        if re.match('NN[*]?', tag) != None:
            NN.append(word)
        if re.match('RB[*]?', tag) != None:
            RB.append(word)
    return list([NN, JJ, RB])

temp = pd.DataFrame(list(data_dict['text'].apply(detect)))
data_dict['NN'], data_dict['JJ'], data_dict['RB'] = temp[:][0], temp[:][1], temp[:][2]


# In[120]:


NN = []

for item in data_dict['NN']:
    NN += item
#count the words
from collections import Counter

#count the words
words=NN

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
print('Unique words: ', len((vocab_to_int_n)))
counts.most_common(20)


# In[121]:


JJ = []
for item in data_dict['JJ']:
    JJ += item
#count the words
from collections import Counter

words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
print('Unique words: ', len((vocab_to_int_j)))
counts.most_common(20)


# In[122]:


#####################
RB = []
for item in data_dict['RB']:
    RB += item
#count the words
from collections import Counter

words=RB

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_r = {word: ii for ii, word in enumerate(vocab, 1)}
#常见R
print('Unique words: ', len((vocab_to_int_r)))
counts.most_common(20)

reviews_ints_r = []
reviews_ints_r.append([vocab_to_int_r[word] for word in RB])


# In[123]:


plt.style.use('ggplot')
tt = ' '.join(NN)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
#plt.title('Reviews',size=20)
plt.show()


# In[124]:


plt.style.use('ggplot')
tt = ' '.join(JJ)
np.random.seed(321)
sns.set(rc={'figure.figsize':(14,8)})
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
wordcloud = WordCloud(background_color="white").generate(tt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
#plt.title('Reviews',size=20)
plt.show()


# In[125]:


sb_R = pd.read_csv('/Users/zzz/Dropbox/未命名文件夹/data/res_by_name/subway_r.csv',encoding = 'latin-1',index_col=0)


# In[126]:


sb_R.head(3)


# In[128]:


sb_R['length'] = sb_R['text'].apply(len)
sb_R.head()


# In[129]:


sb_R.info()


# In[130]:


sb1 = sb_R.sort_values('business_id')
sb1.head(3)


# In[131]:


sb1['stars'].mean()


# In[134]:


s = sb1.groupby('business_id')['stars'].mean()
#s


# In[135]:


num = sb1.groupby('business_id')['stars'].count()
#num


# In[143]:


a = sb1['business_id'].unique()
business_id = []
stars=[]
Num=[]
for i in a:    
    business_id.append(i)
    stars.append(s[i])
    Num.append(num[i])
    #print(i,m[i],num[i])
    
df = pd.DataFrame({'business_id':business_id,'avgstar':stars,'num':Num})
df.head(3) #246


# In[146]:


df4 = df[df['num']>=3]
df4.head(3)  #243/246


# In[147]:


star = np.array([2., 3., 4., 5.])
s2 = sum(df4['avgstar']<=2)
s3 = sum(df4['avgstar']<=3)
s4 = sum(df4['avgstar']<=4)
s5 =sum(df4['avgstar']<=5)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 30,
         }

c = [s2,s3-s2,s4-s3,s5-s4] #[322, 203, 32, 1]
#fig = plt.figure()
figsize = 14,8
figure, ax = plt.subplots(figsize=figsize)

plt.tick_params(labelsize=23)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]


plt.bar(star,c)
plt.xlabel("avg_star", font2)
plt.ylabel("Numbers", font2)
plt.title("Dist of stars", font2)
plt.xlim([1,5])

plt.show()


# In[151]:


new_sb = pd.merge(sb1,df4)
new_sb.head(3) #1980


# In[280]:


l_sb = new_sb[new_sb['avgstar']<=3]
l_sb.to_csv("l_sb.csv")
l_sb = pd.read_csv('l_sb.csv',encoding='latin-1')
l_sb.head(20)


# In[281]:


l_sb.shape[0]


# In[282]:


h_sb = new_sb[new_sb['avgstar']>3]
h_sb.to_csv("h_sb.csv")
h_sb = pd.read_csv('h_sb.csv',encoding='latin-1')


# In[283]:


h_sb.shape[0]


# In[ ]:





# In[250]:


data_dict=l_sb


# In[251]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import nltk 
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english')) 

from nltk import *
data_dict.loc[:,'NN'] =None
data_dict.loc[:,'JJ']=None
data_dict.loc[:,'RB']=None


import numpy as np
def detect(text):
    NN = []
    JJ = []
    RB = []
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    i = 0
    for word, tag in temp:
        if word in stop_words:
            continue
        if re.match('JJ[*]?', tag) != None:
            JJ.append(word)
        if re.match('NN[*]?', tag) != None:
            NN.append(word)
        if re.match('RB[*]?', tag) != None:
            RB.append(word)
    return list([NN, JJ, RB])

temp = pd.DataFrame(list(data_dict['text'].apply(detect)))
data_dict['NN'], data_dict['JJ'], data_dict['RB'] = temp[:][0], temp[:][1], temp[:][2]


# In[252]:


NN = []

for item in data_dict['NN']:
    NN += item
#count the words
from collections import Counter

#count the words
words=NN

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
print('Unique words: ', len((vocab_to_int_n)))
counts.most_common(20)


# In[253]:


JJ = []
for item in data_dict['JJ']:
    JJ += item
#count the words
from collections import Counter

words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
print('Unique words: ', len((vocab_to_int_j)))
counts.most_common(20)


# In[254]:


#####################
RB = []
for item in data_dict['RB']:
    RB += item
#count the words
from collections import Counter

words=RB

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_r = {word: ii for ii, word in enumerate(vocab, 1)}
#常见R
print('Unique words: ', len((vocab_to_int_r)))
counts.most_common(20)

reviews_ints_r = []
reviews_ints_r.append([vocab_to_int_r[word] for word in RB])


# In[255]:


words=NN
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
#print('Unique words: ', len((vocab_to_int_n)))
#counts.most_common(20)


# In[256]:


#l_nouns = pd.read_csv("l_nouns.csv")
a = vocab
nouns = []
freq=[]
Num=[]
#l = counts.sum
for i in a:    
    nouns.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/1420)  

l_nouns = pd.DataFrame({'noun':nouns,'num':Num,'freqs':freq})
l_nouns.head(3)


# In[257]:


words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
#print('Unique words: ', len((vocab_to_int_j)))
#counts.most_common(20)


# In[258]:


a = vocab
adjs = []
freq=[]
Num=[]
for i in a:    
    adjs.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/1420)   
    
l_adjs = pd.DataFrame({'adj':adjs,'num':Num,'freqs':freq})
l_adjs.head(3)


# In[ ]:





# In[259]:


h_sb.head(20)


# In[284]:


data_dict=h_sb


# In[285]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

import nltk 
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english')) 

from nltk import *
data_dict.loc[:,'NN'] =None
data_dict.loc[:,'JJ']=None
data_dict.loc[:,'RB']=None


import numpy as np
def detect(text):
    NN = []
    JJ = []
    RB = []
    text =  word_tokenize(text)
    temp = nltk.pos_tag(text)
    i = 0
    for word, tag in temp:
        if word in stop_words:
            continue
        if re.match('JJ[*]?', tag) != None:
            JJ.append(word)
        if re.match('NN[*]?', tag) != None:
            NN.append(word)
        if re.match('RB[*]?', tag) != None:
            RB.append(word)
    return list([NN, JJ, RB])

temp = pd.DataFrame(list(data_dict['text'].apply(detect)))
data_dict['NN'], data_dict['JJ'], data_dict['RB'] = temp[:][0], temp[:][1], temp[:][2]


# In[286]:


NN = []

for item in data_dict['NN']:
    NN += item
#count the words
from collections import Counter

#count the words
words=NN

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
print('Unique words: ', len((vocab_to_int_n)))
counts.most_common(20)


# In[287]:


JJ = []
for item in data_dict['JJ']:
    JJ += item
#count the words
from collections import Counter

words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
print('Unique words: ', len((vocab_to_int_j)))
counts.most_common(20)


# In[288]:


#####################
RB = []
for item in data_dict['RB']:
    RB += item
#count the words
from collections import Counter

words=RB

# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_r = {word: ii for ii, word in enumerate(vocab, 1)}
#常见R
print('Unique words: ', len((vocab_to_int_r)))
counts.most_common(20)

reviews_ints_r = []
reviews_ints_r.append([vocab_to_int_r[word] for word in RB])


# In[289]:


words=NN
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_n = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_n = []
reviews_ints_n.append([vocab_to_int_n[word] for word in NN])
#print('Unique words: ', len((vocab_to_int_n)))
#counts.most_common(20)


# In[290]:


a = vocab
nouns = []
freq=[]
Num=[]
for i in a:    
    nouns.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/560)   
    
h_nouns = pd.DataFrame({'noun':nouns,'num':Num,'freq':freq})
#h_nouns.to_csv("h_nouns.csv")
#h_nouns = pd.read_csv("h_nouns.csv")
h_nouns.head(3)


# In[291]:


words=JJ
# words wrong datatype
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int_j = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints_j = []
reviews_ints_j.append([vocab_to_int_j[word] for word in JJ])
#常见J
#print('Unique words: ', len((vocab_to_int_j)))
#counts.most_common(20)


# In[292]:


a = vocab
adjs = []
freq=[]
Num=[]
for i in a:    
    adjs.append(i)
    Num.append(counts[i])
    freq.append(counts[i]/560)   
    
h_adjs = pd.DataFrame({'adj':adjs,'num':Num,'freq':freq})
#h_adjs.to_csv("h_adjs.csv")
#h_adjs = pd.read_csv("h_adjs.csv")
h_adjs.head(3)


# In[ ]:





# In[293]:


l_nouns.head()


# In[294]:


h_nouns.head()


# In[295]:


new = pd.merge(l_nouns,h_nouns, on = 'noun')
new['FREQ'] = new['freq']-new['freqs'] #freqs--> l_nouns
new = new.iloc[(-new['FREQ'].abs()).argsort()]
new.head()
#new.to_csv("new.csv")
#new = pd.read_csv("new.csv")
new.head()


# In[325]:


(new['FREQ']<0).sum()


# In[326]:


y = new['FREQ'].head(20)
x = new['noun'].head(20)


# In[328]:


figsize = 50,28.5
figure, ax = plt.subplots(figsize=figsize)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 100,
         }

sns.barplot(x=y,y=x, palette='husl', ax=ax)

plt.tick_params(labelsize=100)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
#plt.barh(x,y)
plt.xlabel("Nouns", font2)
plt.ylabel("Differences of frequences", font2)
plt.title("Top 20 Nouns of Subway", font2)
#plt.xlim([-2,20])
#plt.xticks(rotation=60)

plt.show()


# In[330]:


l_adjs.head()


# In[331]:


h_adjs.head()


# In[332]:


old = pd.merge(l_adjs,h_adjs, on = 'adj')
old['FREQ'] = old['freq']-old['freqs'] #freqs--> l_nouns
old = old.iloc[(-old['FREQ'].abs()).argsort()]
old.head()
#old.to_csv("old.csv")
#old = pd.read_csv("old.csv")
old.head()


# In[333]:


y = old['FREQ'].head(20)
x = old['adj'].head(20)


# In[334]:


figsize = 50,28.5
figure, ax = plt.subplots(figsize=figsize)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 100,
         }



plt.tick_params(labelsize=100)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
#plt.barh(x,y,palette='husl')

sns.barplot(x=y,y=x, palette='husl', ax=ax)

plt.xlabel("Adjs", font2)
plt.ylabel("Differences of frequences", font2)
plt.title("Top 20 Adjs of Subway", font2)
#plt.xlim([-1,20])
#plt.xticks(rotation=45)
plt.show()


# In[ ]:




