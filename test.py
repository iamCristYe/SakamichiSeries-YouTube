import os
res={}
for filename in os.listdir("SakamichiSeries"):
 #   print(filename[-15:-4])
    
    if filename[-15:-4] in res:
        res[filename[-15:-4]].append(filename)
    else:
        res[filename[-15:-4]]=[filename]
        
for video in res:
    if len(res[video])>1:
        print(sorted(res[video]))