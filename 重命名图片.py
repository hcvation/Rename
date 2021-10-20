import os

import time

target1 = ['.jpg','.JPG'];

target2 = ['.png','.PNG'];

dirPath = input('请输入需要进行静态图片整理的文件夹的路径：')
    
os.chdir(dirPath);

olistjpg = [];

olistpng = [];

mlistjpg = [];

mlistpng = [];

olistJPG = [];

olistPNG = [];

mlistJPG = [];

mlistPNG = [];
 
i = 0

j = 0

k = 0

l = 0
    
files = os.listdir(dirPath)

for filename in files:
        
    ext = os.path.splitext(filename)[1]

    createTime = os.path.getmtime(dirPath + os.sep + filename)

    timeArray = time.localtime(createTime)

    t = time.strftime("%Y-%m-%d %H.%M.%S",timeArray)

    if ext in target1 or ext in target2:
        
        os.rename(filename, "o-" + filename)

    if ext in target1:

        olistjpg.append("o-" + os.path.splitext(filename)[0] + '.jpg')

        mlistjpg.append("IMG " + t)
            
    if ext in target2:

        olistpng.append("o-" + os.path.splitext(filename)[0] + '.png')

        mlistpng.append("IMG " + t)

if range(len(mlistjpg)) != 0:

    new_mlistjpg=[v + " - " + str(mlistjpg[:i].count(v) + 1) if mlistjpg.count(v) > 1 else v for i, v in enumerate(mlistjpg)]
        
    for i in range(len(new_mlistjpg)):
            
        os.rename(olistjpg[i], new_mlistjpg[i] + ".jpg")

if range(len(mlistpng)) != 0:

    new_mlistpng=[v + " - " + str(mlistpng[:i].count(v) + 1) if mlistpng.count(v) > 1 else v for i, v in enumerate(mlistpng)]
        
    for j in range(len(new_mlistpng)):
            
        os.rename(olistpng[j], new_mlistpng[j] + ".png")
