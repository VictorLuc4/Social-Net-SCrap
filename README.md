# Social Net SCrap

A powerful tool that collect data from videos on social media.

**Possible improvments :**

- Add a graphic cool visualisation ffor data in the DB
- Automate db creation
- Delete video after usage or send it to s3 
- Reduce video quality before sending it to Google with ffmpeg
- Make google API calls optional
- Add other scrapper (insta / snapchat .. ? )
- Include tiktok-scrapper in this project 
-------
## Run the program

Once you have setup the project with the instructions bellow, you can run the project.

The program takes some time to run (download video then send it to google for inspection). 

```python
usage: sns.py [-h] [-u USER | --hashtag HASHTAG] [-n NUMBER]

optional arguments:
  -h, --help                    show this help message and exit
  -u USER, --user USER          the username of the account you want to scrap.
  --hashtag HASHTAG             the hashtag you want to scrap (without #).
  -n NUMBER, --number NUMBER    the number of videos to scrap (default: 10).
```

Examples : 
```bash
python3 ./sns -u <username> -n 3        # will download 3 videos of <username>
python3 ./sns --hashtag <hashtag> -n 3  # will download 3 videos from #hashtag
```

## Setup to run the program

In order to run this program you will need to : 
* Get your google credentials (optional : needed to call google API)
* Do not forget to enable the API [(see this link)](https://console.developers.google.com/apis/api/videointelligence.googleapis.com/overview)
* Setup Python3 and install the requirements
* Install s3cmd if you want to use with --s3
* Install tiktok-scrapper 
* Install mysql and setup the DB

### Get Google credentials json file

You need to get the json file in the GCP console and add it at the root of this repository under the name `key.json`.

### Setup Python

Env is very useful to avoid a mess on your host when installing lot of strange python packets.

```bash
apt update
apt install virtualenv
virtualenv env -p python3
# to activate
source env/bin/activate
# to check versions
ls env/lib/
# to deactivate
deactivate
```

Then install the requirements : 

```bash
# In your virtual env
python3 -m pip install ./requirements.txt
```


### Install tiktok-scrapper

The tiktok scrapper is a npm command you need to install : 
```bash
npm install -g tiktok-scraper
```

If it is not working try the solution at this link :
https://github.com/drawrowfly/tiktok-scraper/pull/563#issuecomment-852264427


### Install mysql if not done already

```bash
# install mysql
apt install mysql

# Login as root (no password, just press 'enter')
mysql -u root -p 
```

To create the DB : 
```sql
CREATE DATABASE sns;
use sns;
```

You will need to store the db information in a `.env` file : 
```bash
SNS_DB_HOST="127.0.0.1"
SNS_DB_USER="sns"
SNS_DB_PASS="yourpass"
SNS_DB_NAME="sns"
SNS_DB_PORT=3306
```

Then you will need to create all the tables : 

#### Create user table : 
```sql
-- User
CREATE TABLE user (id VARCHAR(255) PRIMARY KEY, nickname VARCHAR(255), avatar VARCHAR(1000), name VARCHAR(255), tikid VARCHAR(255), fans INT, secuid VARCHAR(255), signature VARCHAR(1000), digg INT, verified TINYINT, video INT, heart INT, following INT);

ALTER TABLE user CONVERT TO CHARACTER SET utf8mb4;

--  Music
CREATE TABLE music (id VARCHAR(50) PRIMARY KEY, musicName VARCHAR(255), duration INT, playUrl VARCHAR(500), musicOriginal TINYINT, coverUrl VARCHAR(500), musicAlbum VARCHAR(255), musicAuthor VARCHAR(255));

ALTER TABLE music CONVERT TO CHARACTER SET utf8mb4;

-- Video
CREATE TABLE video (id VARCHAR(50) PRIMARY KEY, userId VARCHAR(255), shareCount INT, commentCount INT, playCount INT, videoUrl VARCHAR(1000), text VARCHAR(1000), coverDynamic VARCHAR(1000), createTime VARCHAR(255), secretID VARCHAR(255), webVideoUrl VARCHAR(1000), diggCount INT, height INT, width INT, duration INT);

ALTER TABLE video CONVERT TO CHARACTER SET utf8mb4;

-- Mention
CREATE TABLE mention (id INT PRIMARY KEY AUTO_INCREMENT, id_video VARCHAR(255), username VARCHAR(255));

ALTER TABLE mention CONVERT TO CHARACTER SET utf8mb4;

-- Hashtag
CREATE TABLE hashtag (id INT PRIMARY KEY AUTO_INCREMENT, id_video VARCHAR(255), name VARCHAR(255), title VARCHAR(255), cover VARCHAR(1000));

ALTER TABLE hashtag CONVERT TO CHARACTER SET utf8mb4;

-- Brand
CREATE TABLE brand (id_video VARCHAR(255) PRIMARY KEY, name VARCHAR(255));
ALTER TABLE brand CONVERT TO CHARACTER SET utf8mb4;

-- Theme
CREATE TABLE theme (id_video VARCHAR(255) PRIMARY KEY, name VARCHAR(255));

ALTER TABLE theme CONVERT TO CHARACTER SET utf8mb4;

-- explicit
CREATE TABLE explicit (id_video VARCHAR(255) PRIMARY KEY, explicit VARCHAR(250));

ALTER TABLE explicit CONVERT TO CHARACTER SET utf8mb4;
```
