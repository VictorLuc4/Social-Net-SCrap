FROM python:3

COPY ./scraper /app/scraper
COPY ./webapp /app/webapp
COPY ./key.json /app/key.json
COPY ./requirements.txt /app/requirements.txt

EXPOSE 5000

RUN apt update
# Install node
RUN apt install curl -y
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt -y install nodejs
# Install npm and the scraper
RUN curl -qL https://www.npmjs.com/install.sh | sh
RUN npm install -g tiktok-scraper
# Install other python requirements
RUN python3 -m pip install -r /app/requirements.txt

ENV FLASK_APP=/app/webapp/app.py

ENTRYPOINT ["flask"]

CMD ["run", "--host=0.0.0.0"]

