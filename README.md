# Simple RSS feed scraper

The `main.py` script can be used with `cron` to monitor any RSS feed that contains an `ETag` header.

It assumes the existence of an `ETag` contained within `latest_etag.txt`. It's very easy to write code to handle whether
such a file exists, but this was meant to be a super quick job.

If the `ETag` has changed, the entire XML representation will be downloaded. The file will be named in this format:

> YYYY-mm-dd-HH-MM.xml

Happy scraping!
