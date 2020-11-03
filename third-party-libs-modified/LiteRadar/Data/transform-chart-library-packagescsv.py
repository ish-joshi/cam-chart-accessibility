text = open("charts-library-packages.csv")

out = []

for line in text:
    line = line.strip()
    lq = line.split(",")
    sha, _, _, _, package = lq
    # print(sha, package)
    assert len(lq) == 5
    out.append(",".join([package, "name", "Charting", "https://ishanjoshi.me"]))

with open('processed-tag-rules-chart-library-grepped-packages', 'w') as of:
    of.write("\n".join(out))
    of.close()
