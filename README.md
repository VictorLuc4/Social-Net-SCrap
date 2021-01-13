# Social Net SCrap

A powerful tool that collect data from videos on social media.

-------

## Setup to run the program
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

```bash
npm install -g tiktok-scraper
```

### Install mysql if not done already

```bash
# install mysql
apt install mysql

# Login as root (no password, just press 'enter')
mysql -u root -p 
```

To create the DB : 
```mysql
CREATE DATABASE sns
use sns
```

Then you will need to create all the tables : 

#### Create user table : 
```
CREATE TABLE user (id VARCHAR(255) PRIMARY KEY, nickname VARCHAR(255), avatar VARCHAR(1000), name VARCHAR(255), tikid VARCHAR(255), fans INT, secuid VARCHAR(255), signature VARCHAR(1000), digg INT, verified TINYINT, video INT, heart INT, following INT);

ALTER TABLE user CONVERT TO CHARACTER SET utf8mb4;
```

#### Create music table : 
```
CREATE TABLE music (id VARCHAR(50) PRIMARY KEY, musicName VARCHAR(255), duration INT, playUrl VARCHAR(500), 
musicOriginal TINYINT, coverUrl VARCHAR(500), musicAlbum VARCHAR(255), musicAuthor VARCHAR(255));

ALTER TABLE music CONVERT TO CHARACTER SET utf8mb4;
```

#### Create video table : 
```
video (id VARCHAR(50) PRIMARY KEY, userId VARCHAR(255), shareCount INT, commentCount INT, playCount INT, videoUrl VARCHAR(1000), text VARCHAR(1000), coverDynamic VARCHAR(1000), createTime VARCHAR(255), secretID VARCHAR(255), webVideoUrl VARCHAR(1000), diggCount INT, height INT, width INT, duration INT);

ALTER TABLE video CONVERT TO CHARACTER SET utf8mb4;
```

#### Create mention table : 

```
CREATE TABLE mention (id INT PRIMARY KEY AUTO_INCREMENT, id_video VARCHAR(255), username VARCHAR(255));

ALTER TABLE mention CONVERT TO CHARACTER SET utf8mb4;
```

#### Create hashtag table : 
```
CREATE TABLE hashtag (id INT PRIMARY KEY AUTO_INCREMENT, id_video VARCHAR(255), name VARCHAR(255), title VARCHAR(255), cover VARCHAR(1000));

ALTER TABLE hashtag CONVERT TO CHARACTER SET utf8mb4;
```

#### Create theme table : 
```
CREATE TABLE theme (id_video VARCHAR(255) PRIMARY KEY, name VARCHAR(255));

ALTER TABLE theme CONVERT TO CHARACTER SET utf8mb4;
```

#### Create explicit table : 
```
CREATE TABLE explicit (id_video VARCHAR(255) PRIMARY KEY, explicit VARCHAR(250));

ALTER TABLE explicit CONVERT TO CHARACTER SET utf8mb4;
```
