# activate virtual env -------------------------------------------------------------------------------------------------
# see requirements.txt for required libraries

import os

activate_this = os.path.expanduser('~/.virtualenvs/feed-scraper/bin/activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

import feedparser
from urllib.request import urlretrieve
import pendulum
import sys

# globals --------------------------------------------------------------------------------------------------------------

url = "https://feeds.feedburner.com/RBloggers?format=xml"


# functions ------------------------------------------------------------------------------------------------------------

def make_file_name():
    current_date_time = pendulum.now()
    file_time = current_date_time.strftime('%Y-%m-%d-%H-%M')
    file_name = file_time + '.xml'
    return file_name


def read_last_etag():
    with open('./github/feed-scraper/latest_etag.txt', 'r') as infile:
        latest_etag = infile.read()
    return latest_etag


def write_new_etag(feed):
    with open('./github/feed-scraper/latest_etag.txt', 'w') as outfile:
        outfile.write(feed.etag)
    print('successfully written!')


def download_xml():
    file_name = make_file_name()
    urlretrieve(url, file_name)


def get_feed():
    return feedparser.parse(url)


def get_feed_status(etag):
    next_feed = feedparser.parse(url, etag=latest_etag)
    print('feed status is ' + str(next_feed.status))
    return next_feed.status


# main script ----------------------------------------------------------------------------------------------------------

print('script running at ' + pendulum.now().strftime('%Y-%m-%d %H-%M'))
latest_etag = read_last_etag()
feed_status = get_feed_status(latest_etag)

if not feed_status == 304:
    print('feed has changed...doing stuff')
    new_feed = get_feed()
    download_xml()
    write_new_etag(new_feed)
    print('\n\n')
    sys.exit()

print('feed has not changed...returning...\n\n')
