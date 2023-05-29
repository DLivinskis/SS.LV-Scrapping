from datetime import date
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
    isExist = os.path.exists(path)
    list_0.append(path)
    list_0.append(isExist)
send_email(str(list_0))
print('Email sent out succesfully')