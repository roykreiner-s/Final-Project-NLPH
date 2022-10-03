
# ---------------------------------------------------------------------------
# This module scrapes relevant text from data sites in hebrew
# ---------------------------------------------------------------------------

import pandas
import requests
import pandas as pd
import matplotlib.pyplot as plt
import time
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
import seaborn as sns
import numpy as np
import re
from itertools import islice




def scrape_thinkil():
    """
    Scraping method for thinkil texts
    :return: dic of {url,author,title,text} of pages in thinkil
    """
    url = "https://thinkil.co.il/texts-sitemap.xml"
    url_response = requests.get(url)
    soup = BeautifulSoup(url_response.text, 'html.parser')

    urls_text = [link.get_text() for link in soup.find_all("loc")][1:6]

    df_dict = {"url": [], "author": [], "title": [], "text": []}

    for url in urls_text:
        time.sleep(1)
        response = requests.get(url)
        soup = BeautifulSoup(response.text)

        df_dict["url"].append(url)
        df_dict["author"].append(
            ",".join([a.text for a in soup.find_all("span", "author-name")]))
        df_dict["title"].append(soup.find("h1", "page-title").text.strip())
        df_dict["text"].append(soup.find("article").text)

    df = pd.DataFrame(df_dict, columns=['url', 'author', 'title', 'text'])

    return df




