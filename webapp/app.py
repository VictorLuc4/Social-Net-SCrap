from flask import Flask
from flask import request, redirect, url_for
from flask import render_template
from flask import jsonify
import os
import mysql.connector

import sqlquery
import utils 

from form import searchform

from dotenv import load_dotenv

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

load_dotenv()

db_host = os.getenv('SNS_DB_HOST', '127.0.0.1')
db_port = os.getenv('SNS_DB_PORT', 3630)
db_user = os.getenv('SNS_DB_USER', 'toto')
db_pass = os.getenv('SNS_DB_PASS', 'toto')
db_name = os.getenv('SNS_DB_NAME', 'toto')

mydb = mysql.connector.connect(
    host = db_host,
    user = db_user,
    port = db_port,
    password = db_pass,
    database = db_name, 
    charset = 'utf8mb4'
)

cursor = mydb.cursor()



@app.route("/", methods=['GET', 'POST'])
def chart():
    searchForm = searchform()
    
    if searchForm.validate():
        return redirect(url_for('search', item=request.form.get('search')))

    ## get top 10 users
    names, videosNb = sqlquery.getTop10UsersByVideoCount(cursor)
    charts = {}
    charts["top10User"] = {'title': "Top 10 users with the most number of videos", \
                        'labels':names, \
                        'values':videosNb, \
                        'legend':'Number of video'}
    
    ## get top 10 brand
    brands, brandsCount = sqlquery.getTop10BrandByCount(cursor)
    charts["top10Brand"] = {'title': "Top 10 brands detected", \
                        'labels':brands, \
                        'values':brandsCount, \
                        'legend':'Number of times detected'}

    ## get explicit
    categories, count = sqlquery.getExplicitCountByCategory(cursor)
    charts["explicitCount"] = {'title': "Number of explicit per category", \
                        'labels':categories, \
                        'values':count, \
                        'legend':'Number of video per category'}

    return render_template('chart.html', charts=charts, title="SNS", form=searchForm)
 

@app.route('/search/<item>')
def search(item="N/A"):
    searchForm = searchform()
    print(item)
    users = sqlquery.searchFromBaseUsername(cursor, item)
    return render_template('result.html', form=searchForm,  item=item, users=users)


@app.route('/custom/<name>')
def custom(name="N/A"):
    searchForm = searchform()
    userInfo = sqlquery.getUserInfo(cursor, name)
    videos = sqlquery.getUserVideos(cursor, name)
    videosInfo = utils.computeVideosInfo(videos)
    explicits = sqlquery.getExplicitVideoUrlFromUser(cursor, name)
    hashtags = sqlquery.getHashtagsCountForUser(cursor, name)
    mentions = sqlquery.getMentionsFromUser(cursor, name)
    brands = sqlquery.getBrandsCountForUser(cursor, name)
    return render_template('custom.html', form=searchForm, info=userInfo, vidinfo=videosInfo, \
                            explicits=explicits, hashtags=hashtags, mentions=mentions, brands=brands)