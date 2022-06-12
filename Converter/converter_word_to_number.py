
from __future__ import print_function, unicode_literals
from tkinter import E

from base import Num2Word_Base
from utils import get_digits, splitbyx

import re


SIZES = {u'מיליון':1000000 , u'מיליארד':1000000000, u'ביליון':1000000000000,
         u'בילארד':1000000000000000, u'טריליון':1000000000000000000,
         u'טריליארד':1000000000000000000000, u'אלף':1000}


def convert_3_digits(words):
    """
    Converts the last 3 digits of the number
    :param x: num to convert
    :param words: words of number list
    :param i: index of current chunk
    """
    
    # remove all start chars for word in words string starting with u'ו'
    filtered_word = []
    for word in words:
        if word.startswith(u'ו'):
            filtered_word.append(word[1:])
        else:
            filtered_word.append(word)


    # join the filtered word to list
    words = ' '.join(filtered_word)


    # convert words to number
    ret = 0

    # hundreds

    if words.find(u'מאה') != -1:
        ret += 100

    elif words.find(u'מאתיים') != -1 :
        ret += 200

    elif words.find(u'שלוש מאות') != -1 or words.find(u'שלושה מאות') != -1:
        ret += 300

    elif words.find(u'ארבע מאות') != -1 or words.find(u'ארבעה מאות') != -1:
        ret += 400

    elif words.find(u'חמש מאות') != -1 or words.find(u'חמישה מאות') != -1:
        ret += 500

    elif words.find(u'שש מאות') != -1 or words.find(u'שישה מאות') != -1:
        ret += 600

    elif words.find(u'שבע מאות') != -1 or words.find(u'שבעה מאות') != -1:
        ret += 700

    elif words.find(u'שמונה מאות') != -1:
        ret += 800

    elif words.find(u'תשע מאות') != -1 or words.find(u'תשעה מאות') != -1:
        ret += 900

    # tens

    if words.find(u'תשעה עשר') != -1 or words.find(u'תשע עשרה') != -1:
        ret += 19
        return ret

    elif words.find(u'שמונה עשר') != -1 or words.find(u'שמונה עשרה') != -1:
        ret += 18
        return ret

    elif words.find(u'שבעה עשר') != -1 or words.find(u'שבע עשרה') != -1:
        ret += 17
        return ret

    elif words.find(u'ששה עשר') != -1 or words.find(u'שש עשרה') != -1:
        ret += 16

    elif words.find(u'חמישה עשר') != -1 or words.find(u'חמיש עשרה') != -1:
        ret += 15
        return ret
    
    elif words.find(u'ארבעה עשר') != -1 or words.find(u'ארבע עשרה') != -1:
        ret += 14
        return ret
    
    elif words.find(u'שלושה עשר') != -1 or words.find(u'שלוש עשרה') != -1:
        ret += 13
        return ret

    elif words.find(u'שניים עשר') != -1 or words.find(u'שתיים עשרה') != -1:
        ret += 12
        return ret

    elif words.find(u'אחת עשר') != -1 or words.find(u'אחד עשרה') != -1:
        ret += 11
        return ret

    elif words.find(u'עשרים') != -1:
        ret += 20

    elif words.find(u' עשר') != -1 or words.find(u'עשרה') != -1:
        ret += 10
        return ret

    elif words.find(u'שלושים') != -1:
        ret += 30

    elif words.find(u'ארבעים') != -1:
        ret += 40

    elif words.find(u'חמישים') != -1:
        ret += 50

    elif words.find(u'שישים') != -1:
        ret += 60

    elif words.find(u'שבעים') != -1:
        ret += 70

    elif words.find(u'שמונים') != -1:
        ret += 80

    elif words.find(u'תשעים') != -1:
        ret += 90

    # ones
    if filtered_word[-1] == (u'אחת') or filtered_word[-1] == (u'אחד'):
        ret += 1

    elif filtered_word[-1] == (u'שתיים') or filtered_word[-1] == (u'שניים'):
        ret += 2

    elif filtered_word[-1] == (u'שלושה') or filtered_word[-1] == (u'שלוש'):
        ret += 3

    elif filtered_word[-1] == (u'ארבעה') or filtered_word[-1] == (u'ארבע'):
        ret += 4

    elif filtered_word[-1] == (u'חמישה') or filtered_word[-1] == (u'חמש'):
        ret += 5

    elif filtered_word[-1] == (u'שישה') or filtered_word[-1] == (u'שש'):
        ret +=6

    elif filtered_word[-1] == (u'שבעה') or filtered_word[-1] == (u'שבע'):
        ret += 7
    
    elif filtered_word[-1] == (u'שמונה') :
        ret += 8

    elif filtered_word[-1] == (u'תשעה') or filtered_word[-1] == (u'תשע'):
        ret += 9


    return ret

def manage_thousends(word):

    if word[0] == u'עשרת':
        return 10000

    if word[0] == u'תשעת':
        return 9000

    if word[0] == u'שמונת':
        return 8000

    if word[0] == u'שבעת':
        return 7000

    if word[0] == u'ששת':
        return 6000

    if word[0] == u'חמשת':
        return 5000

    if word[0] == u'ארבעת':
        return 4000

    if word[0] == u'שלושת':
        return 3000
        

def word2int(words):
    """
    converter - number to word (until THRILIARD)
    :param n: number to convert
    :return: number in words
    """
    ret = 0

     # remove all start chars for word in words string starting with u'ו'
    filtered_word = []
    for word in words.split(' '):
        if word.startswith(u'ו'):
            filtered_word.append(word[1:])
        else:
            filtered_word.append(word)


    # join the filtered word to list
    words = ' '.join(filtered_word)

    
    # split word to words
    words = words.split(' ')

    # run on all words and when find word in SIZES save all words before it and send them to convert_3_digits   
    temp_words = []
    for word in words:
        if word not in SIZES and word != u'אלפים' and word != u'אלפיים':
            temp_words.append(word)

        # special case for thousds u'אלפיים'
        elif word == u'אלפיים':
            ret += 2000

        # special case for thousds u'אלפים'
        elif word == u'אלפים':
            ret += manage_thousends(temp_words)

        else:
            ret += convert_3_digits(temp_words) * SIZES[word]
            temp_words = []

    # add last 3 digits
    ret += convert_3_digits(temp_words)

    return ret

def w2n(word):
    return word2int(word)


def to_currency(n, currency='EUR', cents=True, separator=','):
    raise NotImplementedError()


class Word2Num_HE():
    def to_cardinal(self, word):
        return w2n(word)

    def to_ordinal(self, number):
        raise NotImplementedError()

if __name__ == '__main__':
    yo = Word2Num_HE()
    print(yo.to_cardinal(u' שלוש מאות ועשרים ואחד מיליון שלושים וארבע אלף שלוש מאות ואחד'))






# ------------------- DICS ------------------------------

ZERO = (u'אפס',)

ONES_FEMALE = {
    1: (u'אחת',),
    2: (u'שתים',),
    3: (u'שלש',),
    4: (u'ארבע',),
    5: (u'חמש',),
    6: (u'שש',),
    7: (u'שבע',),
    8: (u'שמונה',),
    9: (u'תשע',),
}

ONES_MALE = {
    1: (u'אחד',),
    2: (u'שניים',),
    3: (u'שלושה',),
    4: (u'ארבעה',),
    5: (u'חמישה',),
    6: (u'שישה',),
    7: (u'שבעה',),
    8: (u'שמונה',),
    9: (u'תשעה',),
}

TENS_FEMALE = {
    0: (u'עשר',),
    1: (u'אחת עשרה',),
    2: (u'שתים עשרה',),
    3: (u'שלש עשרה',),
    4: (u'ארבע עשרה',),
    5: (u'חמש עשרה',),
    6: (u'שש עשרה',),
    7: (u'שבע עשרה',),
    8: (u'שמונה עשרה',),
    9: (u'תשע עשרה',),
}

TENS_MALE = {
    0: (u'עשרה',),
    1: (u'אחד עשר',),
    2: (u'שניים עשר',),
    3: (u'שלושה עשר',),
    4: (u'ארבעה עשר',),
    5: (u'חמישה עשר',),
    6: (u'שישה עשר',),
    7: (u'שבעה עשר',),
    8: (u'שמונה עשר',),
    9: (u'תשעה עשר',),
}

TWENTIES = {
    2: (u'עשרים',),
    3: (u'שלשים',),
    4: (u'ארבעים',),
    5: (u'חמישים',),
    6: (u'ששים',),
    7: (u'שבעים',),
    8: (u'שמונים',),
    9: (u'תשעים',),
}

HUNDRED = {
    1: (u'מאה',),
    2: (u'מאתיים',),
    3: (u'מאות',)
}

THOUSANDS = {
    1: (u'אלף',),
    2: (u'אלפיים',),
    3: (u'שלשת אלפים',),
    4: (u'ארבעת אלפים',),
    5: (u'חמשת אלפים',),
    6: (u'ששת אלפים',),
    7: (u'שבעת אלפים',),
    8: (u'שמונת אלפים',),
    9: (u'תשעת אלפים',),
}

MILIION = u'מיליון'

MILIARD = u'מיליארד'

BILLION = u'ביליון'

BILLIARD = u'בילארד'

TRILION = u'טריליון'

THRILIARD = u'טריליארד'

AND = u'ו'