# ---------------------------------------------------------------------------
# This module filter sentences including numbers (Numbers that appear
# literally)
# ---------------------------------------------------------------------------
import sys
import requests
sys.path.append("C://Users/user/OneDrive/Documents/study/year-3-semster-B/Nlp_hebrew/NLPH_PROJECT/YAP-Wrapper")
from time import sleep
import pandas as pd
from yap_api import YapApi



def split_by_dot(text):
    return text.split('.')



def filter_sentences_with_numbers(texts):
    """
    df filter - filters all sentences and saves only sentences with numbers
    :param texts: data frame
    :return: df of sentences with numbers
    """
    localhost_yap = "http://localhost:8000/yap/heb/joint"
    ret_sentences = []
    for text in texts:
        for sentence in split_by_dot(text):
            sleep(1)
            sentence_text = sentence.replace(r'"', r'\"')
            data = '{{"text": "{}  "}}'.format(sentence_text).encode('utf-8')  # input string ends with two space characters
            headers = {'content-type': 'application/json'}

            try:
                response = requests.get(url=localhost_yap, data=data, headers=headers)
                json_response = response.json()
                if "number" in json_response.json():  # checks sentence has a number in it
                    ret_sentences.append(sentence_text)

            except ConnectionError:
                continue


            # ------------- using Rest API ----------------------
            # sleep(3)
            # s = 'בתוך עיניה הכחולות יש שישה צבעים'
            # # Escape double quotes in JSON.
            # sentence_text = s.replace(r'"', r'\"')
            # url = 'https://www.langndata.com/api/heb_parser?token=c8c085881516eab841a5531e2dda2fcd'
            # _json = '{"data":"' + sentence_text + '"}'
            # headers = {'content-type': 'application/json'}
            # r = requests.post(url, data=_json.encode('utf-8'),headers={'Content-type': 'application/json; charset=utf-8'})
            # if "number" in r.json():
            #     ret_sentences.append(sentence_text)

    return pd.DataFrame(ret_sentences)


