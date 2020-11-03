#  Copyright (c) 2020.
#
#  Ishan Joshi
#
#  This is part of Monash University Honours Project supervised by Dr Chunyang Chen.
#

import shutil


class FileName:
    # android-AbcApplication___1599188627___n_a_-.png
    name, ext, package, ts, meta, has_chart, chart_type, accessible = list("        ")

    def __init__(self, f_name: str, in_dir="", save_it=False):
        name, ext = f_name.split(".")
        self.ext = ext
        self.name = name

        package, ts, meta = name.split("___")

        has_chart, chart_type, accessible = meta.split("_")

        self.package = package
        self.ts = ts
        self.meta = meta

        self.has_chart = has_chart == "y"
        self.chart_type = chart_type
        self.accessible = accessible == "y"

        if save_it and self.has_chart and ext == "png":
            print("Saving this image")
            shutil.copy(in_dir + "/" + f_name, "images_with_charts/" + f_name)

    def get_csv_row(self):
        return ",".join(
            map(str, [self.name, self.ext, self.package, self.ts, self.meta, self.has_chart, self.chart_type,
                      self.accessible]))

    def __str__(self) -> str:
        return "\n".join(
            map(str, [self.name, self.ext, self.package, self.ts, self.meta, self.has_chart, self.chart_type,
                      self.accessible]))

    @staticmethod
    def get_csv_heading():
        return "name,ext,package,ts,meta,has_chart,chart_type,is_accessible,dominant_lib_package"


import os

files = os.listdir(".")

for file in files:

    if not file.endswith("png"):
        continue

    f = FileName(file)
    if f.chart_type == "b":
        shutil.copy(file, "bar_c/{}".format(file))
    elif f.chart_type == "l":
        shutil.copy(file, "line_c/{}".format(file))
    else:
        shutil.copy(file, "pie_c/{}".format(file))
