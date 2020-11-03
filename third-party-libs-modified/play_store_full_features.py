import random
import time
import multiprocessing
from gpapi.googleplay import GooglePlayAPI

# https://github.com/krnick/GooglePlay-API
mail = None
passwd = None
# The gsfId and authSubToken are retrieved from the mail and passwd.
# call api.gsfId and api.authSubToken
gsfId = 4132308869485558804
authSubToken = '0gc-qsIOLGFubtuKlPD9UE-24mcMCanGWWFBFLBF1fiCjNdIAPmFoQDBfQKNDHYJSAesxw.'

api = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="hero2lte")
# api.login(email=mail, password=passwd) # do this the first time!!!
api.login(gsfId=gsfId, authSubToken=authSubToken)

print("Login is ", api.authSubToken != None)
import os

files_present = os.listdir("../outapks")
files_present = set(files_present)


def searchApps(query):
    search_res = api.search(query)
    # region search results print
    apps = []

    for doc in search_res:
        if 'docid' in doc:
            print("doc: {}".format(doc["docid"]))
        for cluster in doc["child"]:
            print("\tcluster: {}".format(cluster["docid"]))
            for app in cluster["child"]:
                apps.append(app["docid"])
    return apps
    # endregion


# result = searchApps("bitcoin")
# print(result)
#
# suggestions = api.searchSuggest("face")
# print(suggestions)


def downloadAndSave(package, filepath=None):
    print("Trying to do package {}".format(package))
    if not filepath:
        filepath = "../outapks/{}.apk".format(package)

    if (package + ".apk") in files_present:
        print("download is already there for {}".format(package))
        return
    # region download and write apk
    apk_bits = api.download(package)
    with open(filepath, 'wb') as o:
        for chunk in apk_bits.get('file')['data']:
            o.write(chunk)
        o.close()

    # endregion


# to_download = "com.gamma.scan"
# downloadAndSave(to_download)
# com.xxmassdeveloper.mpchartexample.apk

def download_keyword_searches(keyword):
    print("Processing keyword {}".format(keyword))
    search_res = searchApps(keyword)
    for app in search_res:
        try:
            downloadAndSave(app)
            time.sleep(random.randint(1, 10))
            print(f"Done with {app} download")
        except Exception as e:
            print("Error downloading cuz {} ... {}".format(str(e), app))
    return search_res


keywords = ["chart", "money", "budget", "split", "stock", "stock tracker", "asx", "maths", "graphs", "weather",
            "prediction",
            "analytics", "business news", "market", "tracker", "fitness tracker", "sleep tracker", "health tracker",
            "chart demos", "charting library demo", "currency converter", "expense", "expense tracker", "money manager",
            "finance manager", "money", "debt tracker", "mortgage calculator", "financial calculator", "emi calculator",
            "cryptocurrency", "crypto", "money challenge", "finance stuff", "invest", "investing guide",
            "market tracker", "business charts", "news charts", "charts", "weather", "weather storm", "weather widget",
            "weather forecast", "surfing forecast", "moon phase", "radar weather usa", "radar weather australia",
            "air quality", "live weather", "home price", "investment house price", "shopping tracker",
            "fitness tracker"]

# Accurate weather Chart

def searchSuggestFlatKW(res):
    return list(map(lambda item: item['suggestedQuery'], res))


# https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
flatten = lambda l: [item for sublist in l for item in sublist]

autocomp = map(lambda kw: searchSuggestFlatKW(api.searchSuggest(kw)), keywords)
values = flatten(autocomp)
print(values)

keywords = values

# downloadAndSave("com.secretapplock.weather")
# 'apps_movers_shakers', offset=20, nb_results=100
# res = api.list("FINANCE", 'apps_topselling_free', nb_results=100)
# res = list(map(lambda dok: dok['docid'], res))
# print(res)
#
# for app in res:
#     downloadAndSave(app)
#     print("downloaded and saved app {}".format(app))
#     time.sleep(2)

# res = api.list("WEATHER", 'apps_topselling_free', nb_results=100, offset=100)
# # res = api.list("WEATHER", 'apps_topselling_free', nb_results=100, offset=100)
# print(res)
keywords.reverse()
print("Starting download.... ;) ")
pool = multiprocessing.Pool(len(keywords) // 4)
res = pool.map(download_keyword_searches, keywords)
print(res)
#
# searchApps("mpandroidchart")

#
# charting_demoes = searchApps("mpandroidchart")
# c = 0
# for app_package in charting_demoes:
#     downloadAndSave(app_package)
#     print(f"Done with {app_package} download")
#
#     if c >= 2:
#         break
#     else:
#         c += 1
#
#     time.sleep(10)
#
# print(charting_demoes)

# adb exec-out uiautomator dump /dev/tty

# adb shell dumpsys window

# https://stackoverflow.com/questions/11201659/whats-the-android-adb-shell-dumpsys-tool-and-what-are-its-benefits

# attempt an auto complete script.

# auto = api.searchSuggest("weather")
# print(auto)
