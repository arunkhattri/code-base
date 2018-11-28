"""
Python Program to arrange files in appropritate sub-dir in a directory.
Creating sub-directories within the directory to organise files in a
common directory.
moving files in appropritate sub-directory.

Application: for stock of different sizes to be arranged in their folder

Author: Arun Kr. Khattri
email: arun.kr.khattri@gmail.com
"""

import shutil
import os
import re


def move_files_in_appropriate_dir(act_dir, pattern):
    """
    Arrange file in appropritate sub-directory
    if sub-directory doesn't exist, will create one with given criterion
    :param act_dir: directory full path
    :param pattern: regex
    """
    # change directory
    os.chdir(action_dir)

    for filename in os.listdir():
        if filename.endswith('.pdf'):
            match = pattern.search(filename).group(0)
            dir_path = "./" + match
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(dir_path)
            # move file
            dest = dir_path + "/" + filename
            shutil.move(filename, dest)


if __name__ == "__main__":
    action_dir = "c:/Users/arunkhattri/Desktop/currentStock/stock_181122"
    pattern = re.compile(r"\d+[xX]\d+")
    move_files_in_appropriate_dir(action_dir, pattern)
