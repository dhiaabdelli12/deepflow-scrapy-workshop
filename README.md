# Scrapy Workshop
This repo contains what we covered in our scraping workshop with scrapy as well as some practice exercices.

TO DO:
- Add an errback function body to handle failed urls by logging them into a text file within the logs/ directory
- Create a spider for tunisieannonce
- Create a spider for genius
- Update the spider to fetch the urls for each post instead of just getting the title
- Add a new method to open each post/song/... and scrape data in details

## Setup

First start by cloning the repo into your local file system

```
git clone https://github.com/dhiaabdelli12/deepflow-scrapy-workshop.git
```

cd into the folder
```
cd deepflow-scrapy-workshop
```

Then you can need to setup the virtual environment using anaconda
```
conda create -n scrapy_workshop python=3.7
```
Activate it

```
conda activate scrapy_workshop
```

Install packages

```
pip install scrapy
```

open the repo with vscode
```
code deepflow-scrapy-workshop
```

## Spider
To run a spider from an already created project use the following command
```
scrapy runspider <spider_file> o ../data/<output_file_name>.json
```

To create a new spider, run the following command
```
scrapy genspider <spider_name> <target_website_url>
```
To run a spider and save the output into a .json file inside the data/ directory

```
scrapy crawl <spider_name> -o ../data/<output_file_name>.json
```


## Using the scrapy shell
To open the scrapy shell
```
scrapy shell
```

then you can launch a request

```
>>> from scrapy import Request
>>> req = Request(<website_url>)
>>> fetch(req)
>>> response.css(...)
```
