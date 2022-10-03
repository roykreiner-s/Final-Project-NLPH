#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function, unicode_literals

from utils import get_digits, splitbyx


THRILIARD_NUMBER = 999999999999999999999

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


def pluralize(n, forms):
    # gettext implementation:
    # (n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2)

    form = 0 if (n % 10 == 1 and n % 100 != 11) else 1 if n != 0 else 2

    return forms[form]


def convert_3_digits(x, words, i, sex):
    """
    Converts the last 3 digits of the number
    :param x: num to convert
    :param words: words of number list
    :param i: index of current chunk
    """

    if x == 0:
        return 0

    n1, n2, n3 = get_digits(x)

    if n3 > 0:
        if n3 <= 2:
            words.append(HUNDRED[n3][0])
        else:
            if sex != 'M':
                words.append(ONES_FEMALE[n3][0] + ' ' + HUNDRED[3][0])
            else:
                words.append(ONES_FEMALE[n3][0] + ' ' + HUNDRED[3][0])

    if n2 > 1:
        words.append(TWENTIES[n2][0])

    if n2 == 1:
        if sex == 'F':
            words.append(TENS_FEMALE[n1][0])
        else:
            words.append(TENS_MALE[n1][0])
    elif n1 > 0 and not (i > 0 and x == 1):
        if sex == 'F':
            words.append(ONES_FEMALE[n1][0])
        else:
            words.append(ONES_MALE[n1][0])

    if len(words) > 1:
        words[-1] = AND + words[-1]


def int2word(n, gender):
    """
    converter - number to word (until THRILIARD)
    :param n: number to convert
    :return: number in words
    """

    if n > THRILIARD_NUMBER:  # doesn't yet work for numbers this big
        raise NotImplementedError()

    if n == 0:
        return ZERO[0]

    words = []

    chunks = list(splitbyx(str(n), 3))
    i = len(chunks)

    for index, x in enumerate(chunks):
        i -= 1

        if i == 0:
            convert_3_digits(x, words, i, gender)

        else:
            if i == 1:  # special case of thousands unit such as 1,2,3,4,5,6,7,8,9.
                n1, n2, n3 = get_digits(x)
                if n2 == 0 and n3 == 0:
                    words.append(THOUSANDS[n1][0])
                    continue

            convert_3_digits(x, words, i, gender)
            if i == 7:
                words.append(THRILIARD)

            elif i == 6:
                words.append(TRILION)

            elif i == 5:
                words.append(BILLIARD)

            elif i == 4:
                words.append(BILLION)

            elif i == 3:
                words.append(MILIARD)

            elif i == 2:
                words.append(MILIION)

            elif i == 1:
                words.append(THOUSANDS[1][0])

    return ' '.join(words)


def n2w(n, gender):
    return int2word(int(n), gender)


def to_currency(n, currency='EUR', cents=True, separator=','):
    raise NotImplementedError()


class Num2Word_HE():
    def to_cardinal(self, number, gender):
        return n2w(number, gender)

    def to_ordinal(self, number):
        raise NotImplementedError()


if __name__ == '__main__':
    yo = Num2Word_HE()
    gender = 'M'
    print(yo.to_cardinal(1016.01, gender))
