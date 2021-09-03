# Social Net SCrap

Social Net SCrap (later called SNS) is an Open Source Intelligence (OSINT) tool, that collect data and metada from videos on social medias from users' profile.

This document is here to list the full documentation of the project!

## Summary

- I. Global overview
    1. Why this project  
    2. Global architechture  
    3. How to install  
    4. Open Source  
  
- II. The scrapper  
    1. How it works  
    2. MySQL setup  
    3. S3 setup  
    4. Google Cloud setup  
    5. Adding more analysis
    6. Usage example  
  
- III. The web interface  
    1. How it works  
    2. Research part  
    3. Scrap part  
    4. Adding more graphs  
  
- IV. To go further  
    1. Add new scrappers   
    2. Things to improve

## I. Global Overview
### 1. Why this project

We decided to create this tool because we think that social media are underestimated and underused to collect personnal data on a specific user or to make links between a group of people. 

Moreover the data usually collected and analyzed is mostly textual or from pictures but it's rare to find tools that analyze the videos. Nowadays, videos are becoming mainstream, as we can see through the increase of video "stories", apps like Vine or TikTok or platform such as Youtube and Twitch.  
Being able to analyze these videos and detect what kind of person is behond, what kind of intentions or ideas are propagated are now a matter. 

SNS is the first step of a bigger project. Where here we scrap only one platform, we want to be able to implement more and more platform. Where here we collect only some types of data and use AI with moderation, we want to collect much more data using AI. And finally where we only display some graphs to present these data, we want to perform a complete deep-analysis of links between people as well as there content and who they are.

### 2. Global architecture

To create SNS, we tried to make each part independent. So the scrapp is working standalone and the web interface too. Also, we packed the project in a container to it is easier to use. Finally we wanted a precise secret management, so we are using environement variable in the container to manage secrets. 

We decided to let the users choose wheter or not they want to store the data in a local or remote database, as well as videos in a object storage or if they wanted to delete them after analysis. 

We also wanted to make SNS usable from the CLI as well as from the web interface. 

Here you can find a schema of the architecture of the project : 

------------------- put schema here -------------------

### 3. How to install

The installation is pretty straightforward ! 

```bash
docker pull sns:latest

docker run -d -p 5000:5000 sns:latest

# You can also add env variable like this : 
docker run -d -p 5000:5000 sns:latest # ------------------- Add env variable command -------------------
```
Then you will be able to access the web interface on `127.0.0.1:5000`.  

Otherwise if you want to use the CLI : 
```bash
docker pull sns:latest

docker run -t -i sns:latest /bin/bash
cd /app/scrapper

# Then you will be in the contaier and you can simply run : 
python3 sns.py --help
```

### 4. Open Source

We wanted to make this project opensource, as we think this should be edited and improved by everyone. Also the size of the project is too big for a small team like us.  
Finally we wanted everyone to be able to use our tool. 


## II. The scrapper
### 1. How it works

------------------- Add the last part -------------------
- explain the process 
- talk about the dependancy

### 2. MySQL setup

------------------- Add the last part -------------------
- scw account
- create database
- create a user
- connect to database
- set the tables
- set utf8
- setup the env credentials


### 3. S3 setup

We decided to allow users to save or not the scrapped videos into an s3 bucket. We think that some people might want to reuse the videos later in a custom process. 
In this documentation we will be using Scaleway Object Storage, so you need an account to connect to [the console of Scaleway](http://console.scaleway.com/).

------------------- Add the last part -------------------
- download s3cmd
- create a bucket on scw
- get your credentials
- configure s3 cmd
- set the config file at the right place
- verify everything works


### 4. Google Cloud setup

------------------- Add the last part -------------------
- create a google cloud account
- add an IAM role
- get the credentials json file
- set the creds at the right place
- talk abour the GOOGLE_APPLICATION_CREDENTIALS env variable
- authorized the use of the API to the

### 5. Adding more analysis

------------------- Add the last part -------------------
- talk about google full potential
- talk about other providers 
- how to implement in the code 

### 6. Usage example

------------------- Add the last part -------------------
- using cli only
- saving to s3
- using hashtag
- using user


## III. The web interface  
### 1. How it works  

------------------- Add the last part -------------------
- explain flask
- explain templates and jinja
- explain the 2 parts search / scrap

### 2. Research part  

------------------- Add the last part -------------------
- how to search
- explain the search engine

### 3. Scrap part  

------------------- Add the last part -------------------
- how to scrap
- what if i do not see the user i scraped

### 4. Adding more graphs  
  
------------------- Add the last part -------------------
- how graph works
- how to add some


## IV. To go further  
### 1. Add new scrappers   

------------------- Add the last part -------------------
- link to insta scraper
- how to implement new scraper



### 2. Things to improve

------------------- Add the last part -------------------
- add ssl certificates to web interface
- create an API
- add more options to the scraper (like music etc)
- add more relevant graphs
- add more scraper
- make the front better



