# from __future__ import print_function, unicode_literals

# import json
# from time import sleep

# import requests
# from yapsdk import Yap

# # todo change it to constants file
# from Converter.converter_number_to_words import Num2Word_HE
# from Converter.converter_word_to_number import Word2Num_HE

# HEBREW_ALPHABETIC_NUMBERS = {"אחד",
#                              "אחת",
#                              "שניים",
#                              "שתיים",
#                              "שלושה",
#                              "שלוש",
#                              "ארבעה",
#                              "ארבע",
#                              "חמישה",
#                              "חמש",
#                              "שישה",
#                              "שש",
#                              "שבע",
#                              "שבעה",
#                              "שמונה",
#                              "תשע",
#                              "תשעה",
#                              "עשר",
#                              "עשרה",
#                              "מאה",
#                              "אלף",
#                              "מליון",
#                              "מיליארד"}


# def check_if_line_contains_numeric_number(line):
#     return any(i.isdigit() for i in line)


# def check_if_line_contains_alphabetic_number(line):
#     return any(word in HEBREW_ALPHABETIC_NUMBERS
#                for word in line.split())

# def build_line_with_number_with_correct_gender(line):

#     # 1. get json from yap
#     r = get_json_from_yap(line)

#     # 2. create dep_tree_dict dic from json
#     dep_tree_dict = get_dep_tree_dict(r)

#     # 4. create md_lattice_dict dic from json
#     md_lattice_dict = get_md_lattice_dict(r)

#     # 5. get co-reference gender of number (female\male) and get number
#     coref_gender, total_number = get_coref_gender_and_number_to_check(dep_tree_dict, md_lattice_dict)

#     # 6. convert word number to number
#     converter_word_to_number = Word2Num_HE()
#     real_num = converter_word_to_number.to_cardinal(total_number)

#     # 7. convert number to word number by gender
#     converter_number_to_word = Num2Word_HE()
#     correct_num_word = converter_number_to_word.to_cardinal(real_num, coref_gender)

#     # 8. build new line
#     line = line.replace(total_number, correct_num_word + " ")

#     # 9. return line
#     return line


# def get_coref_gender_and_number_to_check(dep_tree_dict, md_lattice_dict):
#     total_number = ""
#     coref_gender = ""
#     for key, value in dep_tree_dict.items():
#         for key1, value1 in value.items():
#             if key1 == 'word':
#                 if value1 in HEBREW_ALPHABETIC_NUMBERS:
#                     # get number from json_obj
#                     number = value1
#                     total_number += number
#                     total_number += " "
#                     # get dependent of number
#                     dependent = dep_tree_dict[key]['dependency_arc']
#                     # get gender of dependent
#                     # if dpendent is not part of number
#                     if dep_tree_dict[dependent]['word'] not in HEBREW_ALPHABETIC_NUMBERS:
#                         gender = md_lattice_dict[dependent]['gen']
#                         coref_gender = gender
#     return coref_gender, total_number


# def get_md_lattice_dict(r):
#     md_lattice_dict = r.json().get('md_lattice')
#     md_lattice_dict = json.dumps(md_lattice_dict)
#     md_lattice_dict = json.loads(md_lattice_dict)
#     # convert dict to list of dicts
#     for num in md_lattice_dict:
#         md_lattice_dict[num] = json.loads(json.dumps(md_lattice_dict[num]))
#     return md_lattice_dict


# def get_dep_tree_dict(r):
#     dep_tree_dict = r.json().get('dep_tree')
#     dep_tree_dict = json.dumps(dep_tree_dict)
#     dep_tree_dict = json.loads(dep_tree_dict)
#     # convert dict to list of dicts
#     for num in dep_tree_dict:
#         dep_tree_dict[num] = json.loads(json.dumps(dep_tree_dict[num]))
#     return dep_tree_dict


# def get_json_from_yap(line):
#     # 1. create yap connection
#     sleep(1)
#     # Escape double quotes in JSON.
#     sentence_text = line.replace(r'"', r'\"')
#     url = 'https://www.langndata.com/api/heb_parser?token=c8c085881516eab841a5531e2dda2fcd'
#     _json = '{"data":"' + sentence_text + '"}'
#     headers = {'content-type': 'application/json'}
#     # 2. get json file from yap
#     r = requests.post(url, data=_json.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})
#     return r


# def read_file(file_name, output):
#     with open(file_name, 'r') as file:
#         lines = file.readlines()

#         for line in lines:
#             if (check_if_line_contains_alphabetic_number(line) or check_if_line_contains_numeric_number(line)):
#                 line = build_line_with_number_with_correct_gender(line)
#             else:
#                 print(f"no number in {line}")
#             output += line  # todo change to file and write

#         return output


# def main():
#     line = build_line_with_number_with_correct_gender('נועם קנה חמש עשרה אלף עטים חדשים.')
#     print(line)
#     # output = read_file('file.txt', "")
#     # print(f"output:\n{output}")


# main()
