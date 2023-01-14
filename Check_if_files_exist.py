from datetime import date
import time
import os

today = date.today()
ExcelName = str(today) + ".xlsx"

path1 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Cars/" + str(ExcelName)
path2 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Flats/" + str(ExcelName)
path3 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Flats/Daugavpils/" + str(ExcelName)
path4 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Salidzini_scrapping/" + str(ExcelName)
paths = [path1,path2,path3,path4]
for path in paths:
    isExist = os.path.exists(path)
    print(path)
    print(isExist)
