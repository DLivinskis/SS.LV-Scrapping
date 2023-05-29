import shutil
import requests
from bs4 import BeautifulSoup
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
car_list_1 = ['chevrolet','chrysler','dacia','dodge','fiat','infiniti','jaguar','jeep','mercedes','mini','mitsubishi','porsche','saab','smart','subaru','suzuki','vaz','alfa-romeo','seat','lexus','kia'
]
car_list_2 = ['audi','citroen','ford','hyundai','nissan','opel','peugeot','renault','toyota','volvo','mazda','kia'
]
car_list_3 = ['honda','volkswagen','skoda','land-rover','lexus'
]
car_list_4 = ['others']
car_list_5 = ['bmw']
# car_list_6 = ['seat']
# car_list_7 = []

ExcelName = str(today) + ".xlsx"
list1 = []
list2 = []
ldf = []
list_with_errors = []
def Get_Number_Of_Ads():
    response=requests.get('https://www.ss.com/en/transport/cars')
    print(response.text)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # h4_tags = soup.find_all('h4')
    # for h4 in h4_tags:
    #     span_tags = h4.find_all('span', recursive=False)
    #     print(span_tags)

def Getting_Cars(List_Of_Car_Brands,Table_Number):
    df2 = pd.DataFrame()
    Number_Of_Pages = 200
    for car in List_Of_Car_Brands:

        for x in range(1, Number_Of_Pages):
            try:
                # time.sleep(0.1)
                xhtml = url_get_contents(f"https://www.ss.com/en/transport/cars/{car}/page{x}.html").decode('utf-8')
                p = HTMLTableParser()
                p.feed(xhtml)
                df1 = pd.DataFrame(p.tables[Table_Number])

                print(car)
                # print(df1)
                df1.rename(
                    columns={0: 'nothing', 1: 'nothing1', 2: 'Text', 3: 'Model', 4: 'Year', 5: 'Engine', 6: 'Mileage',
                             7: 'Price'}, inplace=True)

                df1.insert(loc=8,
                           column='Date',
                           value=today)
                df1.insert(loc=9,
                           column='Car Section',
                           value=car)
            except:
                print(car + ' is wrong')
                error=(car + ' is wrong')
                list_with_errors.append(error)

            try:
                df1.drop('nothing', inplace=True, axis=1)
            except:
                'nothing to drop'
            try:
                df1.drop('nothing1', inplace=True, axis=1)
            except:
                'nothing to drop'
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
            print(str(car) + " " + "page" + " " + str(x))
Getting_Cars(car_list_1,6)
Getting_Cars(car_list_2,7)
Getting_Cars(car_list_3,5)
Getting_Cars(car_list_4,2)
Getting_Cars(car_list_5,3)
# Getting_Cars(car_list_6,5)
pd.concat(ldf).to_excel(ExcelName)

print(list_with_errors)
send_email('done\n' + str(list_with_errors))

time.sleep(5)
shutil.move(f"W:\\Coding/PythonProjects\\SS.LV_Scrapping\\{ExcelName}",f"W:\\Coding\\PythonProjects\\ScrappedData\\OneDrive\\Cars")


