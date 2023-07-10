


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #database='joins'
  
)

print(mydb)
mycursor = mydb.cursor(buffered=True)




mycursor.execute("CREATE DATABASE Youtube_API")



# In[10]:


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS youtube_api.Channel (
        name VARCHAR(255),
        id VARCHAR(255),
        subscription_count int(255),
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
        view_count int(255),
        like_count int(255),
        favourite_count int(255),
        comment_count int(255),
        dislike_count int(255),
        duration VARCHAR(255),
        thumbnail VARCHAR(255),
        caption VARCHAR(255)
    )
""")


# In[13]:


import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gnanavel:abcd@cluster0.hqbjvfl.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

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

client = MongoClient(uri, server_api=ServerApi('1')).Youtube_to_SQL.Channel


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

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
   


# In[20]:


import pymongo
db= client.Youtube_to_SQL
records= db.Video


# In[21]:


client = MongoClient(uri, server_api=ServerApi('1')).Youtube_to_SQL.Video

channel_list_id=['CNN','Jayaprakash Raveendran','BBC News','Thanthi TV','T-Series Tamil','Channel 4 News','sonymusicsouth','Saregama Tamil']
y=records.find()
for x in y:
    query= 'INSERT INTO youtube_api.video VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(query, (x['channel_name'], x['id'], x['name'],x['description'],x['tags'],x['published_at'],x['view_count'],x['like_count'],x['favourite_count'],x['comment_count'],x['dislike_count'],x['duration'],x['thumbnail'],x['caption']))
        


# In[22]:


mydb.commit()


# In[23]:


mycursor.execute("select * from youtube_api.video")
for x in mycursor:
  print(x)



