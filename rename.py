import os


def rename(title_file, dir_name):
    with open(title_file) as file:
        titles = file.read().splitlines()
        for filename in os.listdir(dir_name):
            index = int(filename[0:3])
            # skip English titles or already renamed ones
            if filename.startswith(f"{filename[0:5]} {titles[6 + 6 * index]} - {titles[8 + 6 * index]}"):
                continue

            new_name = f"{filename[0:5]} {titles[6 + 6 * index]} - {titles[8 + 6 * index]} - {filename[6:]}"
            try:
                os.rename(f"{dir_name}/{filename}", f"{dir_name}/{new_name}")
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, new_name))


rename("title_N", "乃木坂46全曲 All Songs from Nogizaka46")
rename("title_H", "日向坂46全曲 All Songs from Hinatazaka46")
rename("title_S", "櫻坂46全曲 All Songs from Sakurazaka46")
rename("title_K", "欅坂46全曲 All Songs from Keyakizaka46")
