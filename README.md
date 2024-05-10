# NewsNest
#### This is a simple web-crawler that  is scrapping information from a website and performing filter operation on them

> website used [HackerNews](https://news.ycombinator.com/)

The following information is extracted from the site
- first 30 entries
- order of the entry
- title of the entry
- total no of comments each entry has
- total points each entry has

 > the `news_crawler.py` performs the scrapping and then saves the sanitized data into entries.json file.
data folder contains the json file.


### Additionals

We can perform 2 filter operation on the extracted entries.
`filter_utilities.py` performs these 2 filter operations.

- filter entries that has more than 5 words in the title, ordered by comments
- filter entries that has less than or equal 5 words in the title, ordered by points
- after performing this operation 2 separate folders get created in the data folder with the filtered entries

### Folder Structure

This projects has 3 different folders and some base file in the parent project folder

- **data** folder holds the .json files
- **utils** folder holds json_utils.py that has the basic json_load, json_save, file_name_generator functions; as these functions are basic utility functions and has been used in both crawler and filter operations.
- **tests** folder holds the required test for the filter operation


### Required Commands

- `pip install scrapy`
- `scrapy runspider news_crawler.py`
- `python filter_utilities.py`
- `python -m unittest tests/test_filter_utilities.py`

> helpful resource on scrapy: [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3)
