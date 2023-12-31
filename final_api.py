

import pandas as pd
from googleapiclient.discovery import build
import json
import io
from io import StringIO

Api = 'AIzaSyAMuKIWo-1j9I5s1oCYhubUSN2qSqENc6s'
api_service_name ="youtube"
api_version="V3"

youtube = build("youtube","v3",developerKey=Api)

channel_list=['CNN','AdityaTV','BBCNews','thanthitv','TseriesTamil','Channel4News','SonyMusicSouth','SaregamaTamil']
channel_list_id =[]

f_dict={}
f_list = []
i=0
for c_name in channel_list:
  dict={}
  request= youtube.channels().list(part=["statistics","snippet"],forUsername=c_name)
  response = request.execute()
  name = response['items'][0]['snippet']['title']
  id = response['items'][0]['id']
  sub_count = response['items'][0]['statistics']['subscriberCount']
  c_views = response['items'][0]['statistics']['viewCount']
  c_desc = response['items'][0]['snippet']['description']
  dict['name']=name
  dict['id'] = id
  dict['subscription_count']= sub_count
  dict['channel_views'] = c_views
  dict['channel_description'] = c_desc
  x='channel_'+str(i)
  f_dict[x]=dict
  f_list.append(dict)
  channel_list_id.append(name)
  i = i+1

"""[link text](https://)"""

f_list

f_dict

import json
from google.colab import files
uploaded = files.upload()

# json.loads(uploaded['video_id_1.json'].decode("utf-8"))

v_dict = {}
final_list=[]
for j in range(0,8):
  f_name="video_id_" + str(j+1)+".json"
  video_ids=json.loads(uploaded[f_name].decode("utf-8"))
  v_list = []
  for i in range(0,4):
    x_dict={}
    x= video_ids['items'][i]['id']['videoId']
    request= youtube.videos().list(part=['contentDetails','id','recordingDetails',"statistics","snippet"],id=x )
    response = request.execute()
    #print(response)
    try:
      id = response['items'][0]['id']
    except:
      id = 'null'
    try:
      name = response['items'][0]['snippet']['title']
    except:
      name = 'N/A'
    try:
      description = response['items'][0]['snippet']['description']
    except:
      description = 'N/A'
    try:
      thumbnail = response['items'][0]['snippet']['thumbnails']['default']['url']
    except:
      thumbnail = 'N/A'
    try:
      tags  = str(response['items'][0]['snippet']['tags'])
    except:
      tags = "N/A"
    try:
      pub_at = response['items'][0]['snippet']['publishedAt']
    except:
      pub_at = 'N/A'
    try:
      view_count = response['items'][0]['statistics']['viewCount']
    except:
      view_count = '0'
    try:
      like_count = response['items'][0]['statistics']['likeCount']
    except:
      like_count = '0'
    try:
      fav_count = response['items'][0]['statistics']['favoriteCount']
    except:
      fav_count = '0'
    try:
      comment_count = response['items'][0]['statistics']['commentCount']
    except:
      comment_count = '0'

    try:
      dis_count = response['items'][0]['statistics']['dislikeCount']
    except:
      dis_count = '0'

    try:
      duration = response['items'][0]['contentDetails']['duration']
    except:
      duration = '0'
    try:
      xc = response['items'][0]['contentDetails']['caption']
      if xc.lower() == 'true' :
        caption = 'Available'
      else:
        caption = 'Not Available'
    except:
      caption = 'Not Available'
    x_dict['channel_name'] = channel_list_id[j]
    x_dict['id'] = id
    x_dict['name'] = name
    x_dict['description'] = description
    x_dict['tags'] = tags
    x_dict['published_at'] = pub_at
    x_dict['view_count'] = view_count
    x_dict['like_count'] = like_count
    x_dict['favourite_count'] = fav_count
    x_dict['comment_count'] = comment_count
    x_dict['dislike_count'] = dis_count
    x_dict['duration'] = duration
    x_dict['thumbnail'] = thumbnail
    x_dict['caption'] = caption

    v_list.append(x_dict)

  final_list.append(v_list)
  v_dict[channel_list[j]] = v_list

final_list


import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gnanavel:abcd@cluster0.hqbjvfl.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.Youtube_to_SQL
record = db.Channel

record.insert_many(f_list)

db = client.Youtube_to_SQL
record = db.Video

record.insert_many(final_list)

