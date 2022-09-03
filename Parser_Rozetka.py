from requests import Session
from bs4 import BeautifulSoup
import json
from pprint import pprint


def main():
    url = 'https://rozetka.com.ua/ua/notebooks/c80004/'
    with Session() as session:
        response = session.get(url, timeout=10)
        assert response.status_code == 200, 'bad response'
        print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    breakpoint()

    # title = soup.select('#bookTitle')
    # rating = soup.select('span[itemprop="ratingValue"]')
    picture = soup.select('rz-grid div div a')[0].select('img')[0]['src']

    # description = soup.select('#description')

    # data = {'title': title[0].text.strip(),
    #         'rating': float(rating[0].text.strip()),
    #         'picture': picture[0]['src'],
    #         'description': description[0].text.strip()
    #         }

    pprint(data)
    with open('first_scraper.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()
