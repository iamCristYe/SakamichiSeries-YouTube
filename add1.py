import os

for filename in os.listdir("日向坂46全曲 All Songs from Hinatazaka46"):
    print(filename)
    num = int(filename[0:3])
    if num > 3:
        new_name = f"{num+1:03}{filename[3:]}"
        print(new_name)
        os.rename(
            f"日向坂46全曲 All Songs from Hinatazaka46/{filename}",
            f"日向坂46全曲 All Songs from Hinatazaka46/{new_name}",
        )
