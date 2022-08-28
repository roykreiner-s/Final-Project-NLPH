# # -*- coding: utf-8 -*-


# from hashlib import md5
# import sys
# from converter_number_to_words import Num2Word_HE
# from converter_word_to_number import Word2Num_HE
# from yapsdk import Yap
# import requests
# import json
# import os
# import traceback
# import pip
# from time import sleep
# # from importlib import reload
# # reload(sys)
# # sys.setdefaultencoding('utf-8')


# # ---------------------------

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


# def build_line_with_number_with_correct_gender(dep_tree_dict, md_lattice_dict):
#     print(111)
#     # 1. get json from yap
#     # r = get_json_from_yap(line)
#     print(222)

#     # 2. create dep_tree_dict dic from json
#     # dep_tree_dict = get_dep_tree_dict(dep_tree)
#     print(333)

#     # 4. create md_lattice_dict dic from json
#     # md_lattice_dict = get_md_lattice_dict(md_lattice)

#     # 5. get co-reference gender of number (female\male) and get number
#     coref_gender, total_number = get_coref_gender_and_number_to_check(
#         dep_tree_dict, md_lattice_dict)

#     # 6. convert word number to number
#     converter_word_to_number = Word2Num_HE()
#     real_num = converter_word_to_number.to_cardinal(total_number)

#     # 7. convert number to word number by gender
#     converter_number_to_word = Num2Word_HE()
#     correct_num_word = converter_number_to_word.to_cardinal(
#         real_num, coref_gender)
#     # 8. build new line
#     print("check")
#     print("check2")
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
#                     print(f"value1 {value1}")
#                     # get number from json_obj
#                     number = value1
#                     total_number += number
#                     total_number += " "
#                     # get dependent of number

#                     # print(dep_tree_dict)
#                     dependent = dep_tree_dict[key]['dependency_arc']
#                     # get gender of dependent
#                     # if dpendent is not part of number
#                     print(f"dependent {dependent} type {type (dependent)}")
#                     print(f"key {key} keys {dep_tree_dict.keys()}")
#                     print(f"dep_tree_dict keys {dep_tree_dict}")
#                     if dep_tree_dict[dependent]['word'] not in HEBREW_ALPHABETIC_NUMBERS:
#                         gender = md_lattice_dict[dependent]['gen']
#                         coref_gender = gender
#     return coref_gender, total_number


# def get_md_lattice_dict(md_lattice_dict):
#     # md_lattice_dict = r.get('md_lattice')
#     # md_lattice_dict = json.dumps(md_lattice_dict)
#     # md_lattice_dict = json.loads(md_lattice_dict)
#     # convert dict to list of dicts
#     for num in md_lattice_dict:
#         md_lattice_dict[num] = json.loads(json.dumps(md_lattice_dict[num]))
#     return md_lattice_dict


# def get_dep_tree_dict(dep_tree_dict):
#     # dep_tree_dict = r.get('dep_tree')
#     # dep_tree_dict = json.dumps(dep_tree_dict)
#     # dep_tree_dict = json.loads(dep_tree_dict)
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
#     # _json = _json.encode('utf-8')
#     print("hey2")
#     headers = {'Content-type': 'application/json; charset=utf-8'}
#     # 2. get json file from yap
#     r = requests.post(url, data=_json.encode('utf-8'), headers=headers)
#     print("hey3", r.json())

#     return r


# # ---------------------------


# def run_text(dep_tree, md_lattice):
#     print("run_Text", dep_tree)
#     line = build_line_with_number_with_correct_gender(dep_tree, md_lattice)
#     return line


# def main():
#     dep_tree = sys.argv[1].encode("utf-8")
#     # print(sys.argv[1])
#     print(dep_tree)
#     md_lattice = sys.argv[2]
#     response = run_text(dep_tree, md_lattice)
#     # print(response)


# if (len(sys.argv) < 1):
#     raise Exception("No Arguments")

# # for package in ["requests", "yapsdk"]:
# #     import_or_install(package)

# if __name__ == "__main__":
#     try:
#         main()
#     except:
#         with open("error.txt", "w") as f:
#             f.write(traceback.format_exc())
