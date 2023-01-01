import shutil
import urllib.request
from datetime import date
import time
import pandas as pd
from html_table_parser.parser import HTMLTableParser

today = date.today()


def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


ExcelName = str(today) + ".xlsx"

ldf = []
for x in range(0, 30):
    xhtml = url_get_contents(f"https://www.ss.com/lv/real-estate/flats/daugavpils-and-reg/daugavpils/page{x}.html").decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    # print(p.tables[2])
    # print("\n\nPANDAS DATAFRAME\n")
    # print(pd.DataFrame(p.tables[2]))
    df1 = pd.DataFrame(p.tables[2])
    df1.rename(
        columns={0: 'nothing', 1: 'nothing1', 2: 'Advetisement text', 3: 'District', 4: 'Rooms', 5: 'm2', 6: 'Floor',
                 7: 'Series', 8: 'Price'}, inplace=True)
    df1.insert(loc=9,
               column='Date',
               value=today)
    df1.drop('nothing', inplace=True, axis=1)
    df1.drop('nothing1', inplace=True, axis=1)
    try:
        df1.drop(0, inplace=True, axis=0)
    except:
        'nothing to drop'
    try:
        df1.drop(31, inplace=True, axis=0)
    except:
        'nothing to drop'
    ldf.append(df1)
    print(x)

pd.concat(ldf).to_excel(ExcelName)
time.sleep(5)
shutil.move(f"W:\\Coding/PythonProjects\\SS.LV_Scrapping\\{ExcelName}",f"W:\Coding\PythonProjects\ScrappedData\OneDrive\Flats\Daugavpils")
