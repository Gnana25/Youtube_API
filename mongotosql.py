#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip3 install mysql-connector-python')


# In[6]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #database='joins'
  
)

print(mydb)
mycursor = mydb.cursor(buffered=True)


# In[7]:


mycursor.execute("select * from youtube_api.channel")
print(mycursor)
for x in mycursor:
  print(x)


# In[ ]:


mycursor.execute("CREATE DATABASE Youtube_API")


# In[9]:


mycursor.execute("SHOW tables from youtube_api")

for x in mycursor:
  print(x)


# In[10]:


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS youtube_api.Channel (
        name VARCHAR(255),
        id VARCHAR(255),
        subscription_count VARCHAR(255),
        channel_views VARCHAR(255),
        channel_description VARCHAR(1000)
    )
""")


# In[11]:


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS youtube_api.Video (
        channel_name VARCHAR(255),
        id VARCHAR(255),
        name VARCHAR(255),
        description VARCHAR(255),
        tags VARCHAR(255),
        published_at VARCHAR(255),
        view_count VARCHAR(255),
        like_count VARCHAR(255),
        favourite_count VARCHAR(255),
        comment_count VARCHAR(255),
        dislike_count VARCHAR(255),
        duration VARCHAR(255),
        thumbnail VARCHAR(255),
        caption VARCHAR(255)
    )
""")


# In[12]:


get_ipython().system('pip install pymongo')


# In[13]:


import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gnanavel:abcd@cluster0.hqbjvfl.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#record.insert_one({'name':'gnana','ph':'12345'})
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
   


# In[14]:


import pymongo
db= client.Youtube_to_SQL
records= db.Channel


# In[15]:


# x=records.find_one({"address":"mumbai"})
client = MongoClient(uri, server_api=ServerApi('1')).Youtube_to_SQL.Channel

#print(x)
channel_list_id=['CNN','Jayaprakash Raveendran','BBC News','Thanthi TV','T-Series Tamil','Channel 4 News','sonymusicsouth','Saregama Tamil']
for i in channel_list_id:
    #print(i)
    y=records.find({"name":i})
    for x in y:
        print(x)
        


# In[16]:


# x=records.find_one({"address":"mumbai"})
client = MongoClient(uri, server_api=ServerApi('1')).Youtube_to_SQL.Channel

#print(x)
channel_list_id=['CNN','Jayaprakash Raveendran','BBC News','Thanthi TV','T-Series Tamil','Channel 4 News','sonymusicsouth','Saregama Tamil']
for i in channel_list_id:
    #print(i)
    y=records.find({"name":i})
    for x in y:
        query= 'INSERT INTO youtube_api.channel (name,id,subscription_count,channel_views,channel_description) VALUES (%s,%s,%s,%s,%s)'
        mycursor.execute(query, (x['name'], x['id'], x['subscription_count'],x['channel_views'],x['channel_description']))
        #mycursor.execute(query)
        


# In[17]:


mydb.commit()


# In[18]:


mycursor.execute("select * from youtube_api.channel")
for x in mycursor:
  print(x)



# In[19]:


import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gnanavel:abcd@cluster0.hqbjvfl.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#record.insert_one({'name':'gnana','ph':'12345'})
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
   


# In[20]:


import pymongo
db= client.Youtube_to_SQL
records= db.Video
# x=records.find_one({"address":"mumbai"})


# In[21]:


client = MongoClient(uri, server_api=ServerApi('1')).Youtube_to_SQL.Video

#print(x)
channel_list_id=['CNN','Jayaprakash Raveendran','BBC News','Thanthi TV','T-Series Tamil','Channel 4 News','sonymusicsouth','Saregama Tamil']
y=records.find()
for x in y:
    #print(i)
    query= 'INSERT INTO youtube_api.video VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #print(x)
    mycursor.execute(query, (x['channel_name'], x['id'], x['name'],x['description'],x['tags'],x['published_at'],x['view_count'],x['like_count'],x['favourite_count'],x['comment_count'],x['dislike_count'],x['duration'],x['thumbnail'],x['caption']))
    #mycursor.execute(query)
        


# In[22]:


mydb.commit()


# In[23]:


mycursor.execute("select * from youtube_api.video")
for x in mycursor:
  print(x)



# In[ ]:





# In[ ]:




