# Before runnig make sure you have these tables ready :
# Also after creating table run :
# ALTER TABLE theme CONVERT TO CHARACTER SET utf8mb4;
#
# user
# user (id VARCHAR(255) PRIMARY KEY, nickname VARCHAR(255), avatar VARCHAR(1000), name VARCHAR(255), tikid VARCHAR(255), fans INT, 
# secuid VARCHAR(255), signature VARCHAR(1000), digg INT, verified TINYINT, video INT, heart INT, following INT)
# 
# music
# TABLE music (id VARCHAR(50) PRIMARY KEY, musicName VARCHAR(255), duration INT, playUrl VARCHAR(500), 
# musicOriginal TINYINT, coverUrl VARCHAR(500), musicAlbum VARCHAR(255), musicAuthor VARCHAR(255))
#
# video
# video (id VARCHAR(50) PRIMARY KEY, userId VARCHAR(255), shareCount INT, commentCount INT, playCount INT, 
# videoUrl VARCHAR(1000), text VARCHAR(1000), coverDynamic VARCHAR(1000), createTime VARCHAR(255), secretID VARCHAR(255), 
# webVideoUrl VARCHAR(1000), diggCount INT, height INT, width INT, duration INT)
#
# mention
# mention (id INT PRIMARY KEY AUTO_INCREMENT, id_video VARCHAR(255), username VARCHAR(255))
#
# hashtag
# hashtag (id INT PRIMARY KEY AUTO_INCREMENT, id_video VARCHAR(255), name VARCHAR(255), title VARCHAR(255), cover VARCHAR(1000))
#
# brand
# brand (id_video VARCHAR(255) PRIMARY KEY, name VARCHAR(255))
#
# theme
# theme (id_video VARCHAR(255) PRIMARY KEY, name VARCHAR(255))
#
# explicit
# explicit (id_video VARCHAR(255) PRIMARY KEY, explicit VARCHAR(250))

# - username / hashtag / number

import os 
import sys 
import argparse
# To retreive files from extensions :
import glob
import json
import io
import mysql.connector
from google.cloud import videointelligence_v1 as videointelligence

# Local import
import detector


def fill_args(args):
    nb = 10
    user = ""
    hashtag = ""
    is_user = True

    if args.number: nb = args.number
    
    if args.user and args.user != "":
        user = args.user
        is_user = True

    if args.hashtag and args.hashtag != "":
        hashtag = args.hashtag
        is_user = False
    return {"number":nb, "user":user, "hashtag":hashtag, "is_user":is_user}

def dl_videos(p):
    one = ("user " if p["user"] != "" else "hashtag ")
    two = (p["user"] if p["user"] != "" else p["hashtag"])
    three = str(p["number"])
    cmd = "tiktok-scraper " + one + two + " -n " + three + " -d -t json"
    print(cmd)
    #os.system(cmd)
    
def get_files(p):
    dirname = (p["user"] if p["user"] != "" else "/#"+p["hashtag"])
    pwd = os.getcwd() + dirname
    search_for_videos = pwd + "/*.mp4"
    search_for_json = pwd + "/*.json"
    videos = glob.glob(search_for_videos)
    json = glob.glob(search_for_json)
    return (videos, json)


def parse_json(jsons, mycursor, mydb):
    file = jsons[0]
    with open(file, 'r') as f:
        data = json.load(f)
    
    for elem in data:
        # Insert or Update 
        ### User info ###
        meta = elem["authorMeta"] 
        sql = """
                INSERT INTO user (id, name, nickname, avatar, tikid, fans, secuid, signature, digg, verified, video, heart, following) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE 
                name=%s, nickname=%s, avatar=%s, tikid=%s, fans=%s, secuid=%s, 
                signature=%s, digg=%s, verified=%s, video=%s, heart=%s, following=%s ;
            """
        val = (meta["id"], meta["name"], meta["nickName"], meta["avatar"], meta["id"], 
                meta["fans"], meta["secUid"], meta["signature"], meta["digg"], 
                (1 if meta["verified"] == True else 0), meta["video"], meta["heart"], meta["following"],
                # from here it's for the update part could not find something simpler
                meta["name"], meta["nickName"], meta["avatar"], meta["id"], 
                meta["fans"], meta["secUid"], meta["signature"], meta["digg"], 
                (1 if meta["verified"] == True else 0), meta["video"], meta["heart"], meta["following"])

        mycursor.execute(sql, val)
        mydb.commit()
            
        ### Music info ###
        meta = elem["musicMeta"] 
        sql = """
                INSERT INTO music (id, musicName, duration, playUrl, musicOriginal, coverUrl, musicAlbum, musicAuthor)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE 
                musicName=%s, duration=%s, playUrl=%s, musicOriginal=%s, coverUrl=%s, musicAlbum=%s, musicAuthor=%s;
            """
        val = (meta["musicId"], meta["musicName"], meta["duration"], meta["playUrl"], (1 if meta["musicOriginal"] == True else 0), 
                meta["coverLarge"], meta["musicAlbum"], meta["musicAuthor"],
                # from here it's for the update part could not find something simpler
                meta["musicName"], meta["duration"], meta["playUrl"], (1 if meta["musicOriginal"] == True else 0), 
                meta["coverLarge"], meta["musicAlbum"], meta["musicAuthor"])

        mycursor.execute(sql, val)
        mydb.commit()

        ### Video info ###
        meta = elem
        sql = """
                INSERT INTO video (id, userId, shareCount, commentCount, playCount, videoUrl, text, coverDynamic, createTime, 
                secretID, webVideoUrl, diggCount, height, width, duration)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE 
                userId=%s, shareCount=%s, commentCount=%s, playCount=%s, videoUrl=%s, text=%s, coverDynamic=%s,
                createTime=%s, secretID=%s, webVideoUrl=%s, diggCount=%s, height=%s, width=%s, duration=%s;
            """
        val = (meta["id"], meta["authorMeta"]["id"], meta["shareCount"], meta["commentCount"], meta["playCount"], meta["videoUrl"],
                meta["text"], meta["covers"]["dynamic"], meta["createTime"], meta["secretID"], meta["webVideoUrl"], meta["createTime"],
                meta["videoMeta"]["height"], meta["videoMeta"]["width"], meta["videoMeta"]["duration"],
                # from here it's for the update part could not find something simpler
                meta["authorMeta"]["id"], meta["shareCount"], meta["commentCount"], meta["playCount"], meta["videoUrl"],
                meta["text"], meta["covers"]["dynamic"], meta["createTime"], meta["secretID"], meta["webVideoUrl"], meta["createTime"],
                meta["videoMeta"]["height"], meta["videoMeta"]["width"], meta["videoMeta"]["duration"])

        mycursor.execute(sql, val)
        mydb.commit()

        ### Mentions info ###
        for mention in meta["mentions"]:
            username = mention[1:] # This remove the @ before a mention 
            sql = """
                INSERT INTO mention (id_video, username) 
                VALUES (%s, %s) 
                """
            val = (meta["id"], mention)
            mycursor.execute(sql, val)
            mydb.commit()
        
        # As we insert anyway here, we need to remove duplicates now : 
        # This keeps the highest id
        sql = """
            DELETE t1 FROM mention t1
            INNER JOIN mention t2 
            WHERE 
                t1.id < t2.id AND 
                t1.id_video = t2.id_video AND 
                t1.username = t2.username;
            """
        mycursor.execute(sql)
        mydb.commit()

        ### Hashtags info ###
        for hashtag in meta["hashtags"]:
            sql = """
                INSERT INTO hashtag (id_video, name, title, cover) 
                VALUES (%s, %s, %s, %s)
                """
            val = (meta["id"], hashtag["name"], hashtag["title"], hashtag["cover"])
            mycursor.execute(sql, val)
            mydb.commit()
        
        # As we insert anyway here, we need to remove duplicates now : 
        # This keeps the highest id
        sql = """
            DELETE t1 FROM hashtag t1
            INNER JOIN hashtag t2 
            WHERE 
                t1.id < t2.id AND 
                t1.id_video = t2.id_video AND 
                t1.name = t2.name;
            """
        mycursor.execute(sql)
        mydb.commit()


def get_video_id(video):
    # Get video id
    tmp = video
    p = tmp.find('/')
    while p != -1:
        tmp = tmp[p+1:]
        p = tmp.find('/')
    idv = tmp[:len(tmp) - 4]
    return idv


def google_call(videos, mycursor, mydb):
    client = videointelligence.VideoIntelligenceServiceClient()
    config = videointelligence.types.PersonDetectionConfig(
        include_bounding_boxes=True,
        include_attributes=True,
        include_pose_landmarks=True,
    )
    context = videointelligence.types.VideoContext(person_detection_config=config)

    for video in videos:
        # Open video
        with io.open(video, "rb") as f:
            input_content = f.read()
        # Start the asynchronous request
        print("Sending video " + video + " for analysis...")

        # Maybe here we can send all the videos at the same time
        operation = client.annotate_video(
            request={
                "features": [videointelligence.Feature.LABEL_DETECTION, videointelligence.Feature.LOGO_RECOGNITION, videointelligence.Feature.LABEL_DETECTION, videointelligence.Feature.PERSON_DETECTION, videointelligence.Feature.FACE_DETECTION, videointelligence.Feature.EXPLICIT_CONTENT_DETECTION],
                "input_content": input_content,
                "video_context": context,
            }
        )
        result = operation.result(timeout=90)

        # Retrieve the first result, because a single video was processed.
        annotation_result = result.annotation_results[0]
                
        print("Searching for explicit content...")
        explicit = detector.explicit(annotation_result)
        print("Explicit = ")
        print(explicit)
        
        print("Searching for logo...")
        logos = detector.logo(annotation_result)
        print("Logos = " )
        print(logos)

        print("Searching for theme...")
        themes = detector.theme(annotation_result)
        print("Themes = ")
        print(themes)

        # Saving to DB
        ## Explicit content
        id = get_video_id(video)
        sql = """
                INSERT INTO explicit (id_video, explicit) 
                VALUES (%s, %s) ON DUPLICATE KEY UPDATE
                explicit=%s;
                """
        val = (id, explicit, explicit)
        mycursor.execute(sql, val)
        mydb.commit()

        ## Logos
        for brand in logos:
            sql = """
                INSERT INTO brand (id_video, name) 
                VALUES (%s, %s) ON DUPLICATE KEY UPDATE
                name=%s;
                """
            val = (id, brand, brand)
            mycursor.execute(sql, val)
            mydb.commit()

        ## Theme
        for theme in themes:
            sql = """
                INSERT INTO theme (id_video, name) 
                VALUES (%s, %s) ON DUPLICATE KEY UPDATE
                name=%s;
                """
            val = (id, theme, theme)
            mycursor.execute(sql, val)
            mydb.commit()
        
        exit()
        

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--user", help="the username of the account you want to scrap.")
    group.add_argument("--hashtag", help="the hashtag you want to scrap (without #).")
    parser.add_argument("-n", "--number", help="the number of videos to scrap (default: 10).", type=int)
    args = parser.parse_args()

    # Get arguments 
    params = fill_args(args)
    
    # Dl videos with tiktok-scraper
    dl_videos(params)

    # Setp db 
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sns",
        charset='utf8mb4'
    )
    mycursor = mydb.cursor()

    # retreive videos and json filesn in tabs
    (videos, jsons) = get_files(params)
    
    # parse json/csv file and store the result in DB
    parse_json(jsons, mycursor, mydb)

    # Add a step here to reduce the video quality ? 
    # call google api and store result in DB
    google_call(videos, mycursor, mydb)

    # Delete video after usage ? Send it to s3 ? 


main()