#  Copyright (c) 2020.
#
#  Ishan Joshi
#
#  This is part of Monash University Honours Project supervised by Dr Chunyang Chen.
#

import os
import shutil
from infoextractor import InfoExtracter

APK_DIR = "apks"

# region ADB

from ppadb.client import Client as AdbClient

# Default is "127.0.0.1" and 5037
from ppadb.device import Device

ONEPLUS_SERIAL_NUMBER_ADB = "7d10f9f7"

client = AdbClient(host="127.0.0.1", port=5037)


def get_first_device() -> Device:
    print("Running lambda")
    devices = client.devices()
    return devices[0] if devices else None


# endregion

device = (lambda: get_first_device())()
assert device is not None, "No device found"


# assert device is not None, "Device is not available"


def get_relative_apk_path(apk_name):
    return f"{APK_DIR}/{apk_name}"


def check_valid_apk_name(apk_name):
    """
    :param apk_name: Checks if the apk_name exists in apks/{} directory relataive
    :return: Boolean indication if it exists or not
    """
    return os.path.exists(get_relative_apk_path(apk_name))


def get_valid_chart_or_not() -> bool:
    ok = False
    inp = ""
    while not ok:
        inp = input("Has chart or no? y (has chart)/n (no chart)?").lower()
        ok = inp in {"y", "n"}
        if not ok:
            print("Invalid.. try again")
    return inp == "y"


def get_type_of_chart():
    ok = False
    inp = ""
    valid = set("l,b,p".split(","))
    while not ok:
        inp = input("Type of chart? l (line), b (bar), p (pie)?").lower()
        ok = inp in valid
        if not ok:
            print("Invalid.. try again")
    return inp


def get_is_accessible():
    ok = False
    inp = ""
    valid = set("y,n".split(","))
    while not ok:
        inp = input("Is it accessible? y (yes) / n (no)").lower()
        ok = inp in valid
        if not ok:
            print("Invalid.. try again")
    return inp


def loop_capture_data_until_end(apk_name, package_name):
    ended = False

    while not ended:
        # Ask input any key to log chart or not
        has_chart = get_valid_chart_or_not()
        extras = ""

        if has_chart:
            type_of_chart = get_type_of_chart()
            accessible = get_is_accessible()
            extras += f"y_{type_of_chart}_{accessible}"
        else:
            extras += "n_a_-"

        notes = input("Any additional notes?")

        device.uiautomator_snapshot(apk_name, package_name, extras, notes)

        cont = input("Press any key to continue or type 'end' to stop capture").lower()

        if cont == "end":
            ended = True

    print("Loop capture ended.... :)")


def enter_data_capture():
    # Get the apk file name
    apk_name = input("APK Name Please: ")
    if not check_valid_apk_name(apk_name):
        print(f"No apk found at path {get_relative_apk_path(apk_name)}. Try again.")
        return

    if not apk_name.endswith(".apk"):
        print("Invalid file format. Must end with .apk")
        return

    print(f"Found APK file {apk_name}")

    print("Installing the app now")
    device.install(get_relative_apk_path(apk_name), reinstall=True, grand_all_permissions=True)

    print("Installation complete")
    package_name = InfoExtracter(get_relative_apk_path(apk_name)).package_name()

    device.launch_app(package_name)

    loop_capture_data_until_end(apk_name, package_name)

    input(f"type anything to uninstall package {package_name}")
    device.uninstall(package=package_name)

    print("Deleting file from apks folder...")
    os.remove(get_relative_apk_path(apk_name))


if __name__ == "__main__":
    ended = False

    enter_data_capture()
