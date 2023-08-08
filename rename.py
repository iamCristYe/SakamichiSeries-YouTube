import os
import re
import mutagen


def reverse(dir_name):
    group_letter = dir_name.split()[-1][0]
    for filename in os.listdir("SakamichiSeries"):
        if filename[0] == group_letter:
            first_separator = filename.find("-")
            second_separator = filename.find("-", first_separator + 1)
            third_separator = filename.find("-", second_separator + 1)
            previous_name = f"{filename[1:4]} {filename[third_separator:]}"
            try:
                os.rename(f"SakamichiSeries/{filename}", f"{dir_name}/{previous_name}")
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, previous_name))


def rename(dir_name):
    group_letter = dir_name.split()[-1][0]
    title_file = f"title_{group_letter}"
    with open(title_file) as file:
        titles = file.read().splitlines()
        for filename in os.listdir(dir_name):
            index = int(filename[0:3])

            kanji = titles[14 + 8 * index]
            kanji = kanji.replace("/", "⁄")
            kanji = kanji.replace("-", "–")
            kanji = kanji.replace("?", "？")
            kanji = kanji.replace("!", "！")
            kanji = re.sub(r"\s?\[Vocal\s?\:\s?齋藤飛鳥\s?\(乃木坂46\)\]", "", kanji)

            artist = titles[15 + 8 * index]

            album = titles[16 + 8 * index]
            album = re.sub(r"\s?\(Special Edition\)", "", album)
            album = re.sub(r"\s?\(Complete Edition\)", "", album)
            album = re.sub(r"\s?\(New Song Edition\)", "", album)
            album = re.sub(r"\s?<?\(?初回限定盤>?\)?", "", album)
            album = re.sub(r"\s?<?\(?通常盤>?\)?", "", album)
            album = re.sub(r"\s?<?\(?Type-?\s?[A-E]>?\)?", "", album)
            album = album.replace("?", "？")
            album = album.replace("!", "！")

            new_name = f"{group_letter}{index:03} - {kanji} - {album} - {filename[6:]}"
            try:
                os.rename(f"{dir_name}/{filename}", f"SakamichiSeries/{new_name}")
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, new_name))

            audio = mutagen.File(f"SakamichiSeries/{new_name}", easy=True)
            audio["title"] = kanji
            audio["artist"] = artist
            audio["album"] = album
            audio.save(f"SakamichiSeries/{new_name}")


os.makedirs("SakamichiSeries", exist_ok=True)
os.makedirs("乃木坂46全曲 All Songs from Nogizaka46", exist_ok=True)
os.makedirs("日向坂46全曲 All Songs from Hinatazaka46", exist_ok=True)
os.makedirs("櫻坂46全曲 All Songs from Sakurazaka46", exist_ok=True)
os.makedirs("欅坂46全曲 All Songs from Keyakizaka46", exist_ok=True)

import sys

mode = sys.argv[1]
if mode == "reverse":
    reverse("乃木坂46全曲 All Songs from Nogizaka46")
    reverse("日向坂46全曲 All Songs from Hinatazaka46")
    reverse("櫻坂46全曲 All Songs from Sakurazaka46")
    reverse("欅坂46全曲 All Songs from Keyakizaka46")
if mode == "rename":
    rename("乃木坂46全曲 All Songs from Nogizaka46")
    rename("日向坂46全曲 All Songs from Hinatazaka46")
    rename("櫻坂46全曲 All Songs from Sakurazaka46")
    rename("欅坂46全曲 All Songs from Keyakizaka46")
