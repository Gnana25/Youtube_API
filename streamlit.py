import streamlit as st
import mysql.connector
import pandas as pd
st.set_page_config(page_title= "Youtube Data Harvesting and Warehousing | By Gnanavel",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This app is created by *Gnanavel!*"""})

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="" ,
  port="3306"
)
print(mydb)
mycursor = mydb.cursor(buffered=True) 
st.write("1. What are the names of all the videos and their corresponding channels?")
mycursor.execute("""SELECT distinct name AS video_name, channel_name
                            FROM youtube_api.video
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("2. Which channels have the most number of videos, and how many videos do they have?")
mycursor.execute("""SELECT distinct count(*) AS video_count, channel_name
                            FROM youtube_api.video
                            group by channel_name
                            order by channel_name
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("3. What are the top 10 most viewed videos and their respective channels")
mycursor.execute("""SELECT distinct view_count AS video_view_count, channel_name
                            FROM youtube_api.video
                            group by channel_name,name
                            order by view_count desc
                            limit 10
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("4.How many comments were made on each video, and what are their corresponding video names?")
mycursor.execute("""SELECT distinct comment_count AS comment_count_of_a_video,name as video_name
                            FROM youtube_api.video
                            WHERE comment_count >0
                            """
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("5. Which videos have the highest number of likes, and what are their corresponding channel names? ")
mycursor.execute("""SELECT distinct like_count AS like_count_of_a_video,channel_name,name as video_name
                            FROM youtube_api.video
                            order by like_count desc
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("6. What is the total number of likes and dislikes for each video, and what are their corresponding video names? ")
mycursor.execute("""SELECT distinct like_count AS like_count_of_a_video,dislike_count as dislike_count_of_a_video,channel_name,name as video_name
                            FROM youtube_api.video
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("7. Which videos have the highest number of comments, and what are their corresponding channel names?")
mycursor.execute("""SELECT channel_name , max(comment_count)
                            FROM youtube_api.video
                            group by channel_name
                            ORDER by channel_name
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("8. What is the total number of views for each channel, and what are their corresponding channel names?")
mycursor.execute("""SELECT distinct channel_views, name as  channel_name
                            FROM youtube_api.channel
                            ORDER by channel_views >0
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("9. Which is the top 10 comment count &their corresponding channel names")
mycursor.execute("""SELECT distinct channel_name AS Channel_Name,id AS Video_ID,comment_count AS Comment_Count
                            FROM youtube_api.video
                            ORDER BY comment_count DESC
                            LIMIT 10""")
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
st.write("10. What is the subcription count for each channel")
mycursor.execute("""SELECT distinct name AS Channel_Name,subscription_count
                            FROM youtube_api.channel
                            """)
df = pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
st.write(df)
