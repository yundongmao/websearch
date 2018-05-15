import json
import re
#
import collections

# f = open("./project_files/testing.json")
# a = f.readline()
# dict = json.loads(a)
# print (len(dict))
# print (dict[0])


f2 = open("./project_files/documents.json")
a = f2.readline()
doc_dict = json.loads(a)
# for s in doc_dict[0]["text"]:
#     print(s)
print(doc_dict[380]["text"][0])
print(doc_dict[380]["text"][1])
print(doc_dict[380]["text"][2])
print(doc_dict[380]["text"][3])
print(doc_dict[380]["text"][4])
print(doc_dict[380]["text"][5])
# print(len(doc_dict))
# "".isalpha()
# # "".split([" ",","])
# print ("a a b c,d".split())
# print (re.split(",|\.| |\?|!","a a b ?sdjflksjfl! I love you!c,d"))
# collections.defaultdict(0)
