def checkIT(filename):
    text = open("json-resses/{}".format(filename)).read()
    count_charts = text.count("chart")
    return filename, count_charts, text

import os

files = os.listdir("json-resses")

print(len(files))

import multiprocessing

pool = multiprocessing.Pool(processes=32)

out = pool.map(checkIT, files)

for file in out:
    name, count, text = file
    if count > 0:
        print(file)
        print("_______________________________________\n\n\n\n\n")
