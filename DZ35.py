import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.ixbt.com/news/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("div", class_ = "g-grid")

    for el in elements:
        name = el.find("h3")
        if name:
            print("1",name.text)

if __name__ == '__main__':
    main()



def main():
    url = "https://www.ixbt.com/news/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("div", class_ = "b-content")

    for el in elements:
        name = el.find("a")
        if name:
            print(name.text)

if __name__ == '__main__':
    main()



def main():
    url = "https://www.ixbt.com/news/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("div", class_ = "b-content b-content__pagecontent")

    for el in elements:
        name = el.find("h3")
        if name:
            print(name.text)

if __name__ == '__main__':
    main()

