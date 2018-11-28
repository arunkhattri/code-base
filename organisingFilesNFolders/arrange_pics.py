# arranging files on windows

import os
import sys
import re
import shutil

# Arranging Note2 backup pictures year and month wise...


def copy_file(path, look):
    folder = os.listdir(look)
    print("Total Files: {}".format(len(folder)))
    mth = ["jan", "feb", "mar", "apr", 'may', 'jun', 'jul',
           'aug', 'sep', 'oct', 'nov', 'dec']
    date_pattern = re.compile(("(\d{8})"))
    dirs = set()
    counter = 0
    for f in folder:
        # match pattern
        m = date_pattern.search(f)
        # print(m)
        # if m is not date, save it in assorted dir
        if m is None:
            #TODO: save in assorted dir
            continue
        else:
            digits = m.group(0)
            # print(digits)
            year = digits[:4]
            month = int(digits[4:6])
            mth_str = mth[month - 1]
            dir_name = os.path.join(os.sep, path, year, mth_str)
            dirs.add(dir_name)

            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            shutil.copy((look + "/" + f), (dir_name + "/" + f))
            counter += 1
            # print(counter)

            if counter % 50 == 0:
                print("done {} images".format(counter))
    
    print("Moving File Complete. Done {} images".format(counter))
    # return(dirs)


if __name__ == "__main__":
    # look = "/home/arunkhattri/Dropbox/Videos/personalVideos"
    look = "/home/arunkhattri/Dropbox/images/MinooNote2_06092017"
    path = "/home/arunkhattri/Dropbox/images/MinooNote2"
    copy_file(path, look)
