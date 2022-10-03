# This module returns the number in words in the correct format
# using the reference gender of the number


# ------------------------------ DICS  -----------------------------------------------

# without "ו"
ONE_WORD = 1

ZERO = (u'אפס',)

ONES_FEMALE_TO_MALE = {
    u'אחת': u'אחד',
    u'שתים': u'שניים',
    u'שלש': u'שלושה',
    u'ארבע': u'ארבעה',
    u'חמש': u'חמישה',
    u'שש': u'שישה',
    u'שבע': u'שבעה',
    u'שמונה': u'שמונה',
    u'תשע': u'תשעה'
}

ONES_MALE_TO_FEMALE = {
    u'אחד': u'אחת',
    u'שניים': u'שתים',
    u'שלושה': u'שלש',
    u'ארבעה': u'ארבע',
    u'חמישה': u'חמש',
    u'שישה': u'שש',
    u'שבעה': u'שבע',
    u'שמונה': u'שמונה',
    u'תשעה': u'תשע'
}

TENS_FEMALE_TO_MALE = {
    u'עשר': u'עשרה',
    u'אחת עשרה': u'אחד עשר',
    u'שתים עשרה': u'שניים עשר',
    u'שלש עשרה': u'שלושה עשר',
    u'ארבע עשרה': u'ארבעה עשר',
    u'חמש עשרה': u'חמישה עשר',
    u'שש עשרה': u'שישה עשר',
    u'שבע עשרה': u'שבעה עשר',
    u'שמונה עשרה': u'שמונה עשר',
    u'תשע עשרה': u'תשעה עשר'
}

TENS_MALE_TO_FEMALE = {
    u'עשרה': u'עשר',
    u'אחד עשר': u'אחת עשרה',
    u'שניים עשר': u'שתים עשרה',
    u'שלושה עשר': u'שלש עשרה',
    u'ארבעה עשר': u'ארבע עשרה',
    u'חמישה עשר': u'חמש עשרה',
    u'שישה עשר': u'שש עשרה',
    u'שבעה עשר': u'שבע עשרה',
    u'שמונה עשר': u'שמונה עשרה',
    u'תשעה עשר': u'תשע עשרה'
}

# includes "ו"

ONES_FEMALE_TO_MALE_AND = {
    u'ואחת': u'ואחד',
    u'ושתים': u'ושניים',
    u'ושלש': u'ושלושה',
    u'וארבע': u'וארבעה',
    u'וחמש': u'וחמישה',
    u'ושש': u'ושישה',
    u'ושבע': u'ושבעה',
    u'ושמונה': u'ושמונה',
    u'ותשע': u'ותשעה'
}

ONES_MALE_TO_FEMALE_AND = {
    u'ואחד': u'ואחת',
    u'ושניים': u'ושתים',
    u'ושלושה': u'ושלש',
    u'וארבעה': u'וארבע',
    u'וחמישה': u'וחמש',
    u'ושישה': u'ושש',
    u'ושבעה': u'ושבע',
    u'ושמונה': u'ושמונה',
    u'ותשעה': u'ותשע'
}

TENS_FEMALE_TO_MALE_AND = {
    u'ועשר': u'ועשרה',
    u'ואחת עשרה': u'ואחד עשר',
    u'ושתים עשרה': u'ושניים עשר',
    u'ושלש עשרה': u'ושלושה עשר',
    u'וארבע עשרה': u'וארבעה עשר',
    u'וחמש עשרה': u'וחמישה עשר',
    u'ושש עשרה': u'ושישה עשר',
    u'ושבע עשרה': u'ושבעה עשר',
    u'ושמונה עשרה': u'ושמונה עשר',
    u'ותשע עשרה': u'ותשעה עשר'
}

TENS_MALE_TO_FEMALE_AND = {
    u'ועשרה': u'ועשר',
    u'ואחד עשר': u'ואחת עשרה',
    u'ושניים עשר': u'ושתים עשרה',
    u'ושלושה עשר': u'ושלש עשרה',
    u'וארבעה עשר': u'וארבע עשרה',
    u'וחמישה עשר': u'וחמש עשרה',
    u'ושישה עשר': u'ושש עשרה',
    u'ושבעה עשר': u'ושבע עשרה',
    u'ושמונה עשר': u'ושמונה עשרה',
    u'ותשעה עשר': u'ותשע עשרה'
}


def correct_number_in_words(word_number, gender):
    """
    correct the number writing in words due to his reference gender
    :param word_number: number writing in words
    :param gender: reference gender
    :return: correct number in hebrew words
    """

    word_number_list = word_number.split(' ').trim()

    # correct if only one word in 3 last digits of number
    if len(word_number_list) == ONE_WORD:
        last_word = word_number_list[0]
        if gender == "male":
            if last_word in ONES_FEMALE_TO_MALE:
                return ONES_FEMALE_TO_MALE[last_word]
            elif last_word in ONES_FEMALE_TO_MALE_AND:
                return ONES_FEMALE_TO_MALE_AND[last_word]

        elif gender == "female":
            if last_word in ONES_MALE_TO_FEMALE:
                return ONES_MALE_TO_FEMALE[last_word]
            elif last_word in ONES_MALE_TO_FEMALE_AND:
                return ONES_MALE_TO_FEMALE_AND[last_word]

        return last_word


    if len(word_number_list) > ONE_WORD:
        two_last_word = ' '.join(word_number_list[:2])

        if gender == "male":
            if two_last_word in ONES_FEMALE_TO_MALE:
                return ONES_FEMALE_TO_MALE[last_word]
            elif last_word in ONES_FEMALE_TO_MALE_AND:
                return ONES_FEMALE_TO_MALE_AND[last_word]

        elif gender == "female":
            if last_word in ONES_MALE_TO_FEMALE:
                return ONES_MALE_TO_FEMALE[last_word]
            elif last_word in ONES_MALE_TO_FEMALE_AND:
                return ONES_MALE_TO_FEMALE_AND[last_word]

        return last_word


    # check if some word includes "ו" at the beginning
    for w in wo
    if word_last[0] == u'ו':
        word_last = word_last[1:]
        auto_correct(word_last, gender)

    else:
        auto_correct(word_last, gender)


def auto_correct(word_number, gender):
    """
    :return: correct unit number in hebrew words
    """
