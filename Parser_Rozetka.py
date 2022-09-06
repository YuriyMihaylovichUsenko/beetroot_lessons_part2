from requests import Session
from bs4 import BeautifulSoup
from pprint import pprint


url = 'https://rozetka.com.ua/ua/notebooks/c80004/'


def respons_soup(link):
    with Session() as session:
        response = session.get(link, timeout=10)
        assert response.status_code == 200, 'bad response'
        print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def create_data(soup):
    all = soup.select('rz-catalog-tile', class_='ng-star-inserted')
    data = {}
    for i in range(60):
        picture = all[i].select(
            'div a', class_='goods-tile__picture ng-star-inserted'
        )[0].select('img')[0]['src']
        name = all[i].select(
            'div a', class_='goods-tile__picture ng-star-inserted'
        )[0].select('img')[0]['title']
        ugly_price = all[i].select(
            'span', class_='goods-tile__price-value')[-2].text.strip()
        pritty_price = ''.join(ugly_price.split('\xa0'))
        data[i] = {'name': name, 'picture': picture, 'price': pritty_price}
    return data


def main():
    soup = respons_soup(url)
    # breakpoint()
    data = create_data(soup)
    pprint(data)


if __name__ == '__main__':
    main()
