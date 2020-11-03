#  Copyright (c) 2020.
#
#  Ishan Joshi
#
#  This is part of Monash University Honours Project supervised by Dr Chunyang Chen.
#

import os


def process_type():
    files = os.listdir("pie_c")
    accessible_files = filter(lambda file: file.endswith("y.png"), files)
    accessible_files = list(accessible_files)
    # print("Total files:", files)
    print("Total files:", len(files), " Accessible files:", len(accessible_files))


if __name__ == "__main__":
    process_type()
