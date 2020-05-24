# Python scraper with BeautifulSoup

A scraper for scraping football matches played by a football player

* [Data Source](https://footballia.net/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
beautifulsoup4==4.9.1
lxml==4.5.1
soupsieve==2.0.1
tqdm==4.46.0
urllib3==1.25.9

```
A requirements.txt file has been created, use the following command to install these packages
```
pip install -r requirements.txt
```

### Running the scraper

1. Navigate to the project folder and run the following command
```
python3 football_scraper.py
```
2. A matches.txt file will be created in the directory with all the matches

## Built With

* [Python 3.7](https://docs.python.org/3.7/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#xml) - Web scraping library

