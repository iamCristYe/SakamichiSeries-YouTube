import os
import re
import mutagen


def reverse(dir_name):
    group_letter = dir_name.split()[-1][0]
    for filename in os.listdir("SakamichiSeries"):
        if filename[0] == group_letter:
            first_separator = filename.find("-")
            second_separator = filename.find("-", first_separator + 1)
            previous_name = f"{filename[1:4]} {filename[second_separator:]}"
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
            album = re.sub(r"\s?<?\(?コンプリートパック>?\)?", "", album)
            album = re.sub(r"\s?<?\(?Type-?\s?[A-E]>?\)?", "", album)
            album = album.replace("？", "?")
            album = album.replace("！", "!")
            album = re.sub(r"\s$", "", album)
            album = re.sub(r"\!\s+", "!", album)

            album_list = {
                "NS": [
                    "ぐるぐるカーテン",
                    "おいでシャンプー",
                    "走れ!Bicycle",
                    "制服のマネキン",
                    "君の名は希望",
                    "ガールズルール",
                    "バレッタ",
                    "気づいたら片想い",
                    "夏のFree&Easy",
                    "何度目の青空か?",
                    "命は美しい",
                    "太陽ノック",
                    "今、話したい誰かがいる",
                    "ハルジオンが咲く頃",
                    "裸足でSummer",
                    "サヨナラの意味",
                    "インフルエンサー",
                    "逃げ水",
                    "いつかできるから今日できる",
                    "シンクロニシティ",
                    "ジコチューで行こう!",
                    "帰り道は遠回りしたくなる",
                    "Sing Out!",
                    "夜明けまで強がらなくてもいい",
                    "しあわせの保護色",
                    "僕は僕を好きになる",
                    "ごめんねFingers crossed",
                    "君に叱られた",
                    "Actually...",
                    "好きというのはロックだぜ!",
                    "ここにはないもの",
                    "人は夢を二度見る",
                    "おひとりさま天国",
                    "Monopoly",
                ],
                "NA": [
                    "透明な色",
                    "それぞれの椅子",
                    "生まれてから初めて見た夢",
                    "今が思い出になるまで",
                ],
                "NUA": ["僕だけの君 ~Under Super Best~"],
                "NBA": [
                    "Time flies",
                ],
                "HS": [
                    "キュン",
                    "ドレミソラシド",
                    "こんなに好きになっちゃっていいの?",
                    "ソンナコトナイヨ",
                    "君しか勝たん",
                    "ってか",
                    "僕なんか",
                    "月と星が踊るMidnight",
                    "One choice",
                    "Am I ready?",
                ],
                "HKA": [
                    "走り出す瞬間",
                ],
                "HA": ["ひなたざか", "脈打つ感情"],
                "SS": [
                    "Nobody's fault",
                    "BAN",
                    "流れ弾",
                    "五月雨よ",
                    "桜月",
                    "Start over!",
                    "承認欲求",
                ],
                "SA": [
                    "As you know?",
                ],
                "KS": [
                    "サイレントマジョリティー",
                    "世界には愛しかない",
                    "二人セゾン",
                    "不協和音",
                    "風に吹かれても",
                    "ガラスを割れ!",
                    "アンビバレント",
                    "黒い羊",
                ],
                "KA": [
                    "真っ白なものは汚したくなる",
                ],
                "KBA": [
                    "永遠より長い一瞬 ～あの頃、確かに存在した私たち～",
                ],
            }

            flag = True
            for album_category in album_list:
                if album in album_list[album_category]:
                    album = f"{album_category}{album_list[album_category].index(album)+1:02} - {album}"
                    flag = False
            if flag:
                album = f"Other - {album}"

            new_name = f"{group_letter}{index:03} - {kanji} - {filename[6:]}"
            try:
                os.rename(f"{dir_name}/{filename}", f"SakamichiSeries/{new_name}")
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, new_name))

            audio = mutagen.File(f"SakamichiSeries/{new_name}", easy=True)
            audio["title"] = f"{group_letter}{index:03} - {kanji}"
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
    reverse("欅坂46全曲 All Songs from Keyakizaka46")
    reverse("櫻坂46全曲 All Songs from Sakurazaka46")
    reverse("日向坂46全曲 All Songs from Hinatazaka46")
if mode == "rename":
    rename("乃木坂46全曲 All Songs from Nogizaka46")
    rename("欅坂46全曲 All Songs from Keyakizaka46")
    rename("櫻坂46全曲 All Songs from Sakurazaka46")
    rename("日向坂46全曲 All Songs from Hinatazaka46")
