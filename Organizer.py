import os
import shutil
path=input("Enter the Path:")
listoffiles=os.listdir(path)
#print(listoffiles)
for file in listoffiles:
    name,ext=os.path.splitext(file)
    print(name)
    print(ext)
    ext=ext[1:]
    print(ext)
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+file)