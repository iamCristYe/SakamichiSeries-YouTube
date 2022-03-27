# one time fix for 01 to 001

import os


def add_leading_zero(dir_name):
    for filename in os.listdir(dir_name):
        try:
            os.rename(f"{dir_name}/{filename}", f"{dir_name}/0{filename}")
        except OSError as err:
            print("OS Error: {0}{1} already exists.".format(err))


add_leading_zero("日向坂46全曲 All Songs from Hinatazaka46")
add_leading_zero("櫻坂46全曲 All Songs from Sakurazaka46")
add_leading_zero("欅坂46全曲 All Songs from Keyakizaka46")
