from parser import build_line_with_number_with_correct_gender, run_text
import random
from time import sleep


def create_syntethic_data():

    # open new tsv file named "data_synthetic.tsv"
    data_file = open("data_synthetic.tsv", "w")
    # create table with 2 columns in top of the tsv file named "Sentence" and "Label"
    data_file.write("Sentence\tLabel\n")

    heb_words = get_hebrew_words()

    # create a list of 1000 sentences
    sentences = []
    for i in range(300):
        try:
            sleep(3)
            # choose random number between 1 to 10000000000
            number = random.randint(1, 100)
            # if (i % 2 == 0):
            #     number = random.randint(1, 100)
            # if (i % 3 == 0):
            #     number = random.randint(1, 1000)
            # convert the number to string
            number = str(number)
            # choose random word from heb_words
            word = random.choice(heb_words)
            # create a sentence with the number and the word
            sentence = "" + number + " " + word

            # change sentence by male
            male_sentence = build_line_with_number_with_correct_gender(
                sentence, 'M')
            sleep(3)
            # change sentence by women
            female_sentence = build_line_with_number_with_correct_gender(
                sentence, 'F')
            sleep(3)
            real_sentence = build_line_with_number_with_correct_gender(
                sentence)

            if male_sentence == real_sentence:
                # add to sentences sentence with value 1
                sentences.append([male_sentence, 1])
            else:
                sentences.append([male_sentence, 0])

            if female_sentence == real_sentence:
                # add to sentences sentence with value 1
                sentences.append([female_sentence, 1])
            else:
                sentences.append([female_sentence, 0])
        except:
            continue

    # write Sentence and Label to data_file
    for sentence in sentences:
        data_file.write(sentence[0] + "\t" + str(sentence[1]) + "\n")

    # close data_file
    data_file.close()

# get hebrew bag of words


def get_hebrew_words():
    stop_path = "hebrew_names.txt"
    with open(stop_path, encoding="utf-8") as in_file:
        lines = in_file.readlines()
        res = [l.strip() for l in lines]
    return res


if __name__ == '__main__':
    create_syntethic_data()
