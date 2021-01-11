FROM debian:latest

# install pip3
RUN apt update 
RUN apt install -y python3-pip
RUN apt install -y nodejs
RUN apt install -y npm

# install s3cmd
RUN pip3 install s3cmd
# install flask
RUN pip3 install flask

# install tiktok-scrapper
RUN npm i -g tiktok-scraper

# setup config for s3cmd
#COPY ./.s3cfg /root/.s3cfg

# api stuff
WORKDIR /usr/src/app

COPY . .

EXPOSE 5000

# setup env to run flask
ENV FLASK_APP app.py

CMD [ "flask", "run", "--host", "0.0.0.0" ]