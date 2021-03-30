import glob
import os

files = glob.glob("**/*.png", recursive = True)

indx = 0
for file in files:
    new_file = file
    # new_file =file.replace(".PNG", ".png")
    new_file =new_file.replace(" ", "_")
    os.rename(file, new_file)
    # if indx>10:
    #     break
    indx+=1
