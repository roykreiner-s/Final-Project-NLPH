
from yapsdk import Yap


# todo change it to constants file
HEBREW_ALPHABETIC_NUMBERS = {"אחד",
                             "אחת",
                             "שניים",
                             "שתיים",
                             "שלושה",
                             "שלוש",
                             "ארבעה",
                             "ארבע",
                             "חמישה",
                             "חמש",
                             "שישה",
                             "שש",
                             "שבע",
                             "שבעה",
                             "שמונה",
                             "תשע",
                             "תשעה",
                             "עשר",
                             "עשרה",
                             "מאה",
                             "אלף",
                             "מליון",
                             "מיליארד"}


def check_if_line_contains_numeric_number(line):
    return any(i.isdigit() for i in line)


def check_if_line_contains_alphabetic_number(line):
    return any(word in HEBREW_ALPHABETIC_NUMBERS
               for word in line.split())


# def gen_yap_api(text):
#         text= text.replace(r'"', r'\"')
#         url = f'https://www.langndata.com/api/heb_parser?token={yap_token}'
#         _json='{"data":"'+text.strip()+'"}'
#         headers = {'content-type': 'application/json'}
#         sleep(0.1)
#         r = requests.post(url,  data=_json.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})
#         json_obj=r.json()
#         return json_obj.get('segmented_text')


def build_line_with_number_with_correct_gender(line):
    # todo [noamkesten] build new line
    return line


def read_file(file_name, output):
    with open(file_name, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if (check_if_line_contains_alphabetic_number(line) or check_if_line_contains_numeric_number(line)):
                line = build_line_with_number_with_correct_gender(line)
            else:
                print(f"no number in {line}")
            output += line  # todo change to file and write

        return output


def main():
    output = read_file('file.txt', "")
    print(f"output:\n{output}")


main()
