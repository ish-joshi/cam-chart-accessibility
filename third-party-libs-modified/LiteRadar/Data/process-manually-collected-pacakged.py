file = open("package-names.csv")


def dot_package_to(package):
    return "L" + str(package).replace(".", "/")


for line in file:
    line = line.strip()
    if line == "packagename,library,website":
        continue

    info = line.split(",")
    package, name, url = info
    assert len(info) == 3

    print(",".join([dot_package_to(package), name, "Charting", url]))
