# Aditya Halder

import os
import sys
from os import listdir, mkdir

from AdityaHalder.console import LOGGER


def dirr():
    if "šššššššš" not in listdir():
        LOGGER(__name__).warning(
            f"š„ šš”š¢š¬ ššš©šØ š¢š¬ ššØš­ šš«š¢š š¢š§šš„ā\nšš„ššš¬š šš¬š šš«š¢š š¢š§šš„ ššš©šØ āØ..."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("š„ šš„š„ šš¢š«ššš­šØš«š¢šš¬ šš©ššš­šš āØ...")
