from datetime import date, timedelta
import time
import os
import pandas as pd
from sending_email import send_email

today = date.today()
ExcelName = str(today) + ".xlsx"
df = pd.DataFrame(columns=['name', 'Status'])

list_0 = []

path1 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Cars/" + str(ExcelName)
path2 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Flats/" + str(ExcelName)
path3 = "W:\Coding\PythonProjects\ScrappedData\OneDrive\Daugavpils/" + str(ExcelName)
path4 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Salidzini_scrapping/" + str(ExcelName)
path5 = "W:/Coding/PythonProjects/ScrappedData/OneDrive/Flats_Riga_Region/" + str(ExcelName)
paths = [path1,path2,path3,path4,path5]

for path in paths:
    try:
        isExist = os.path.exists(path)
        size_bytes = os.path.getsize(path)
        size_bytes = size_bytes/1024
        size_bytes = round(size_bytes, 2)
        list_0.append(path)
        list_0.append(isExist)
        list_0.append(size_bytes)
    except:
        list_0.append('no files')
send_email(str(list_0))
# print(list_0)
print('Email sent out succesfully')
