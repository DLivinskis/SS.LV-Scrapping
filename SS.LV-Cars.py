#Libraries
from bs4 import BeautifulSoup #to parse HTML data
import os
import shutil
import requests #to get HTML data
import xlsxwriter #to save scrapped data to the excel spreadsheet
from datetime import date #to get today's date which will be used in naming of the file
import re #to get rid of text in price column
from time import sleep
#/Libraries

#Variables section:
today = date.today() #variable for name of the end fiel
current_path_to_file = str(os.getcwd()) + "\\" + str(today) + "_cars.xlsx" #path form which to move the file
List_with_links = [] #empty list where links will be stored
url = "https://www.ss.com/en/transport/cars/alfa-romeo/" #url from which we will be getting information
start_phrase = "/msg/en" #Variable that will be used to sort out only the links for ads. We will skip all other unrealdted links
#/Variables section

print("Today's date:", today) #print out today's date in terminal; optional step


response = requests.get(url)
data_for_soup = response.text
soup = BeautifulSoup(data_for_soup, "html.parser")
print(soup.text)

# def Getting_Links(class_to_search, subclass_to_search='',start_phrase='',string_to_add_in_the_beginning=''):
#     start_phrase = start_phrase
#     string_to_add_in_the_beginning = string_to_add_in_the_beginning
#     names = soup.find_all(class_to_search)
#     for name in names:
#         entry_to_populate = (name.get(subclass_to_search))
#         List_with_links.append(entry_to_populate)
#     updated_list = [name for name in List_with_links if name.startswith(start_phrase)]
#     updated_list = [string_to_add_in_the_beginning + name for name in List_with_links if name.startswith(start_phrase)]
#     print(updated_list)
#
# Getting_Links("a","href","/msg/en","https://www.ss.com/")

# def Getting_b(class_to_search,subclass_to_search):
#     names = soup.find_all(class_to_search)
#     for name in names:
#         entry_to_populate = (name.get(subclass_to_search))
#         List_with_links.append(entry_to_populate)
#     print(List_with_links)
#
# Getting_b("a","b")