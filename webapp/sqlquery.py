# Recupérer les utilisateurs avec un contenu possiblement explicit
# SELECT user.nickname FROM user INNER JOIN video ON video.userId = user.id INNER JOIN explicit ON explicit.id_video = video.id;

# Get url of possible explicit videos
# SELECT webVideoUrl from  video INNER JOIN explicit ON explicit.id_video = video.id limit 3;

# convert time in seconds to date format : 
# import datetime
# datetime.datetime.fromtimestamp(1549634152).strftime('%c')

# Get user specific by item
# SELECT name FROM user INNER JOIN video INNER JOIN explicit WHERE explicit.explicit='LIKELY' AND explicit.id_video=video.id AND video.userId=user.id;

# Get top 10 brand and count
def getTop10BrandByCount(cursor):
    cursor.execute("select name, count(*) from brand group by name limit 10;")
    result = cursor.fetchall()
    return [str(name) for name, count in result], [count for name, count in result]

# get explicit count 
def getExplicitCountByCategory(cursor):
    cursor.execute("select explicit, count(*) from explicit group by explicit;")
    result = cursor.fetchall()
    return [str(name) for name, count in result], [count for name, count in result]

# get top10 nickname by video count desc
def getTop10UsersByVideoCount(cursor):
    cursor.execute("select nickname, video from user order by video desc limit 10;")
    users = cursor.fetchall()
    return [names for names, nb in users], [nb for names, nb in users]


# search engine from username
def searchFromBaseUsername(cursor, username):
    username = '%' + username + '%'
    cursor.execute("select nickname, name from user where nickname like %s or name like %s", (username,username))
    users = cursor.fetchall()
    result = [{k:v} for k, v in users]
    return result


# get user basic informations
def getUserInfo(cursor, name):
    toSelect = ["nickname", "name", "fans", "signature", "verified", "video", "heart", "following"]
    cursor.execute("select nickname, name, fans, signature, verified, video, heart, following from user where name=%s;", (name,))
    userInfo = cursor.fetchall()
    zipped = zip(toSelect, userInfo[0])
    dicted = dict(zipped)
    return dicted

# get all videos data from a user
def getUserVideos(cursor, name):
    cursor.execute("select * from video inner join user where video.userId = user.id and user.name = %s;", (name,))
    results = cursor.fetchall()
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    final_res = []
    for item in results:
        zipped = zip(field_names, item)
        final_res.append(dict(zipped))
    return final_res

# Get all the explicit videos for a specific user
def getExplicitVideoUrlFromUser(cursor, name):
    cursor.execute("""  \
                    select webVideoUrl, explicit from video join explicit inner join user  \
                    WHERE user.name=%s and video.userId=user.id and video.id=explicit.id_video \
                    and (explicit.explicit='VERY_LIKELY' or explicit.explicit='LIKELY' or explicit.explicit='POSSIBLE');
                    """, (name,)) # or explicit.explicit='POSSIBLE'
    results = cursor.fetchall()
    results = dict(results)
    if results == {}:
        return {'N/A':'N/A'}
    return results

# Get all the hashtag and the count for a specific user
def getHashtagsCountForUser(cursor, name):
    cursor.execute("""  \
                    select hashtag.name, count(*) from hashtag inner join video inner join user where \
                    user.id=video.userId and hashtag.id_video=video.id and user.name=%s \
                    group by hashtag.name; \
                    """, (name,))
    results = cursor.fetchall()
    results = dict(results)
    if results == {}:
        return {'N/A':'N/A'}
    return results

# Get all mentions count for a specific user
def getMentionsFromUser(cursor, name):
    cursor.execute("""\
                    select username, count(*) from mention inner join video inner join user \
                    where user.id=video.userId and mention.id_video=video.id and user.name=%s \
                    group by username; \
                    """, (name,))
    results = cursor.fetchall()
    results = dict(results)
    if results == {}:
        return {'N/A':'N/A'}
    return results


# get all brand count that appears for a users
def getBrandsCountForUser(cursor, name):
    cursor.execute("""\
                    select brand.name, count(*) from brand inner join video inner join user \
                    where user.id=video.userId and brand.id_video=video.id and user.name=%s \
                    group by brand.name; \
                    """, (name,))

    results = cursor.fetchall()
    results = dict(results)
    if results == {}:
        return {'N/A':'N/A'}
    return results