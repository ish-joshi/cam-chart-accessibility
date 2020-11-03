import os

files_to_check = os.listdir("json-resses")

print(files_to_check)
import json


def hasChart(file_name):
    fptr = open("json-resses/{}".format(file_name))
    jso = json.load(fptr)
    # print(jso)
    return file_name, jso, jso['count'] > 0


# r = hasChart("com.popularapp.periodcalendar.apk.json")
# print(r)

import multiprocessing

pool = multiprocessing.Pool(10)
which = pool.map(hasChart, files_to_check)
which = list(filter(lambda deets: deets[2], which))

which = list(filter(lambda deets: not (str(deets[0]).startswith(("9", "1", "7", "2", "3", "fourrrrr"))), which))
print()
ll = []
for i, app in enumerate(which):
    print(i + 1, app)
    ll.append(app[0].replace(".json", ""))

print("There are {} apps with charts".format(len(which)))

# print(ll)
