import requests
from bs4 import BeautifulSoup

def scraper(word):
    word = word.replace(' ', '-')
    url = f"https://www.dictionary.com/browse/{word}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    answer = soup.findAll('span', {'class': 'one-click-content css-nnyc96 e1q3nk1v1'})[0].text

    return answer

f = open("ENGELS HW/engelsHW.txt", "r")
for line in f.readlines():
    print(line, '-', end="")

    try:
        print(scraper(line))
    except:
        print('couldnt find it')

    print()
