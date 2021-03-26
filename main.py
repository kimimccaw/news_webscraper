import requests
import sys
from datetime import date
from bs4 import BeautifulSoup


def web_scrapping():
    args = sys.argv[1:] 
    for i in args:
        r = requests.get(i)
    
    soup = BeautifulSoup(r.text, 'html.parser')


    #title of webpage
    title = soup.title
    title_text = title.get_text()
    print(title_text)

    paragraph = soup.find_all('p')

    for i in paragraph:
        print(i.get_text())

    write_in_txt = str(input("Do you want a copy of the news in .txt ? (Yes or No) : "))
    filename = "News_" + str(date.today()) + ".txt"


    if write_in_txt.upper() == 'yes'.upper():
        openF = open(filename, "w+")
        openF.write("******************\n")
        openF.writelines(str(date.today()))
        openF.write("\n******************\n\n\n")
        openF.write("Title: ")
        openF.write(title_text)
        openF.write("\n\n")
        for i in paragraph:
            openF.write(i.get_text())
            openF.write("\n")

        print("Your news has been saved in", filename)
    else:
        print("Your news hasn't been saved")



if __name__ == "__main__":
    web_scrapping()
