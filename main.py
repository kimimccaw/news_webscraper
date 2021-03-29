import requests
import sys
from datetime import date
from bs4 import BeautifulSoup

def extract_url(args):
    url = ''.join(args)
    return url

def scrape_html_from_url(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')
    return soup


if __name__ == "__main__":
    url = extract_url(sys.argv[1:]) 
    html = scrape_html_from_url(url)

    #title of webpage
    title_text = html.title.get_text()
    print("Title: " , title_text)

    paragraph = html.find_all('p')

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



