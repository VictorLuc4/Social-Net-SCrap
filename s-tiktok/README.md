
# Tiktok scraper

Based on [this repository from github](https://github.com/drawrowfly/tiktok-scraper).

## Run the scraper

```bash
cd s-tiktok
docker build -t "tiktok-scraper"
docker run -p 5000:5000 -d tiktok-scraper

# The to try its running : 
curl 127.0.0.1:5000
```

## Contribute 

1. Go to s-tiktok directory : 
```bash
cd s-tiktok
```
2. Create a virtual env and activate it. If not installed run `apt install virtualenv` before.
```bash
virtualenv env -p python3
# to activate
source env/bin/activate
# to deactivate
deactivate
```
3. Install requirements : 
```bash
pip3 install -r ./requirements.txt
``` 