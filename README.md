# Social Net SCrap

A powerful tool that use AI to detect bad stuff in videos from tiktok, instagram stories and snapchat.

## Prerequisites

You will need to install some tools : 
```bash
tuto : 
https://heartbeat.fritz.ai/detecting-objects-in-videos-and-camera-feeds-using-keras-opencv-and-imageai-c869fe1ebcdb

yolo : 
https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
```


-------

## Setup virtual environment

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

## Install tiktok-scrapper

```bash
npm install -g tiktok-scraper
```
