# Recupérer les utilisateurs avec un contenu possiblement explicit
# SELECT user.nickname FROM user INNER JOIN video ON video.userId = user.id INNER JOIN explicit ON explicit.id_video = video.id;

# Get url of possible explicit videos
# SELECT webVideoUrl from  video INNER JOIN explicit ON explicit.id_video = video.id limit 3;

# convert time in seconds to date format : 
# import datetime
# datetime.datetime.fromtimestamp(1549634152).strftime('%c')

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