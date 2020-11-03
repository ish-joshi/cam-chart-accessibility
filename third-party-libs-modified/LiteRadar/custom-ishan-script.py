import json
from literadar import LibRadarLite
import os

done = os.listdir("json-resses")
done = list(map(lambda f: str(f).replace(".json", ""), done))

done = set(done)

files = os.listdir("../../outapks")

# files = ["heart-rate-monitor_4.3.apk"]


# print("% done is {}".format(len(done)/len(files)))
print(len(done) * 100 / len(files))

fs = set(files)

inters = fs.intersection(done)

fs = fs - inters

files = list(fs)

print(files)

PROCESSES_COUNT = 24

print("% done is {}".format(len(done)/len(files)))


# files = files[0:4]


def processFile(file):
    try:
        print("processing {}".format(file))
        full_path = "../../outapks/{}".format(file)
        iron_apk_path = full_path
        lrd = LibRadarLite(iron_apk_path)
        res = lrd.compare()
        count = res['count']

        f = open("json-resses/{}.json".format(file), 'w')
        res = json.dumps(res, indent=4, sort_keys=True)
        # print(res)
        f.write(res)
        f.close()
        print("Done {} with count {} and res \n{}".format(iron_apk_path, count, res))
        f.flush()

    except Exception as e:
        print("")


import multiprocessing

pool = multiprocessing.Pool(min(PROCESSES_COUNT, len(files)))
pool.map(processFile, files)

#
# iron_apk_path = ""
# lrd = LibRadarLite(iron_apk_path)
# res = lrd.compare()
# print(json.dumps(res, indent=4, sort_keys=True))
