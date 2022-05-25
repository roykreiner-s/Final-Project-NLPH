# ---------------------------------------------------------------------------
# This module filter sentences including numbers (Numbers that appear
# literally)
# ---------------------------------------------------------------------------
import sys
import requests
sys.path.append("C://Users/user/OneDrive/Documents/study/year-3-semster-B/Nlp_hebrew/NLPH_PROJECT/yap_wrapper")
from time import sleep
import pandas as pd



def split_by_dot(text):
    return text.split('.')

def filter_sentences_with_numbers(texts):
    ip = '127.0.0.1:8000'
    localhost_yap = "http://localhost:8000/yap/heb/joint"

    for text in texts:
        for sentence in split_by_dot(text):
            sleep(3)

            s = 'בתוך עיניה הכחולות ירח חם תלוי'
            # Escape double quotes in JSON.
            sentence_text = sentence.replace(r'"', r'\"')
            url = 'https://www.langndata.com/api/heb_parser?token=c8c085881516eab841a5531e2dda2fcd'
            _json = '{"data":"' + sentence_text + '"}'
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=_json.encode('utf-8'),headers={'Content-type': 'application/json; charset=utf-8'})
            print(r.json())






