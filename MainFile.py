import shutil
import urllib.request
from datetime import date
import time
import pandas as pd
from html_table_parser.parser import HTMLTableParser
from sending_email import send_email

today = date.today()


def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


ExcelName = str(today) + ".xlsx"

ldf = []
def Scrapping_Apartments (area,destination_path,table_number):
    df2 = pd.DataFrame()
    for x in range(1,200):
        xhtml = url_get_contents(f"https://www.ss.com/en/real-estate/flats/{area}/all/page{x}.html").decode('utf-8')
        p = HTMLTableParser()
        p.feed(xhtml)
        # print(p.tables[2])
        # print("\n\nPANDAS DATAFRAME\n")
        # print(pd.DataFrame(p.tables[2]))
        df1 = pd.DataFrame(p.tables[table_number])
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
        if df1.equals(df2):
            break
        df2 = df1
        ldf.append(df1)
        print(area + ' page ' + str(x))

    pd.concat(ldf).to_excel(ExcelName)
    time.sleep(5)
    shutil.move(f"W:\\Coding/PythonProjects\\SS.LV_Scrapping\\{ExcelName}",
                destination_path)
try:
    Scrapping_Apartments("riga",f"W:\\Coding\\PythonProjects\\ScrappedData\\OneDrive\\Flats",2)
except:
    send_email('problem with Riga Apartments')
ldf = []
try:
    Scrapping_Apartments("riga-region",f"W:\\Coding\\PythonProjects\\ScrappedData\\OneDrive\\Flats_Riga_Region",6)
except:
    send_email('problem with Riga Area Apartments')

