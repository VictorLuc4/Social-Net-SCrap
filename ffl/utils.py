
def computeVideosInfo(videos):
    import datetime

    durations = []
    shares = []
    comments = []
    plays = []
    descSize = []
    webUrls = []
    created = []
    weekdays = []
    hours = []

    for video in videos: 
        durations.append(video["duration"])
        shares.append(video["shareCount"])
        comments.append(video["commentCount"])
        plays.append(video["playCount"])
        descSize.append(len(video["text"]))
        webUrls.append(video["webVideoUrl"])
        created_date = datetime.datetime.fromtimestamp(int(video["createTime"]))
        fulldate = created_date.strftime('%c')
        day = created_date.strftime('%A')
        hour = created_date.strftime('%H')
        created.append(fulldate)
        weekdays.append(day)
        hours.append(hour)

    bubble = getBubbleFromDaysAndHours(weekdays, hours)
    videoNum = len(videos)
    infos = {'videoNum':videoNum, \
            'duration_av':int(sum(durations)/videoNum), \
            'share_av': int(sum(shares)/videoNum), \
            'plays_av': int(sum(plays)/videoNum), \
            'comments_av': int(sum(comments)/videoNum), \
            'descSize_av': int(sum(descSize)/videoNum), \
            'web_urls' : webUrls, \
            'created_date': created, \
            'weekdays' : weekdays, \
            'hours' : hours, \
            'bubble': bubble }

    return infos

def getBubbleFromDaysAndHours(days, hours):
    #days = ['Tuesday', 'Tuesday', 'Tuesday', 'Wednesday', 'Wednesday']
    #hours = [2, 8, 8, 2, 2]
    daysDict = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
    infos = {}
    for i in range(0, len(days)):
        dnum = daysDict[days[i]]

        if dnum in infos.keys():
            # the day exist, so we need to check for the hour now
            if hours[i] in infos[dnum].keys():
                # hour for the day exists so we increase the occurence
                infos[dnum][hours[i]] += 1
            else:
                # hour doesn't exist so we add it
                infos[dnum][hours[i]] = 1
        else:
            # the day doesn't exist so we add it with the hour 
            infos[dnum] = {hours[i]: 1}

    # Then we need to transform in in  a x, y, r dictionary
    bub = []
    for y, val in infos.items():
        tmp = {}
        for x, z in val.items():
            bub.append({'x':x, 'y':y, 'r':z*5})

    return bub