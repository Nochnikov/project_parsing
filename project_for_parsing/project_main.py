import requests
from bs4 import BeautifulSoup
import simple_colors

if __name__ == '__main__':
    url = "https://sxodim.com/almaty/search-events?date_from=01.01.2024&date_to=31.01.2024"

    response_title = requests.get(url)

    date_title = response_title.text

    soup_title = BeautifulSoup(date_title, 'html.parser')

    page_title = soup_title.find('h1', class_='page-title')

    print(simple_colors.cyan(f"{page_title.text.strip()}? Вот вам несколько подборок от журнала 'Давай Сходим!'", 'bold'))
    print()

    for page in range(1, 11):

        payload = {
            'page': page
        }

        response = requests.get(url, params=payload)

        data = response.text

        soup = BeautifulSoup(data, 'html.parser')

        impression_items = soup.find('div', class_="page-content")
        event_titles = impression_items.find_all('a', class_='impression-card-title')
        event_infos = impression_items.find_all('div', class_='impression-card-info')

        for i in range(len(event_titles)):
            print(f'Событие: {event_titles[i].text.strip()}', simple_colors)
            print(f'Информация:  {event_infos[i].text.strip()}')
            print('====================')

        if page+1 == 11:
            pass
        else:
            print()
            print(simple_colors.blue(f'Следующая страница, {page + 1}', ['bold', 'underlined']))
            print()
    # event_title = soup.find(name='div', class_='impressions')
    # event_title = event_title.find_all(name='div', class_='impression-card ')
    #
    # for page_title in event_title:
    #     info = page_title.text.strip().split('\n')
    #     print(f"{info[0]}? По версии журнала 'Давай сходим'".strip())
    #     event_title = page_title.find_all('a', class_='impression-card-title')
    #     event_price_location_date = page_title.find_all('div', 'impression-card-info')
    #     # print(f"{info}")
    # # print("По версии журнала 'Давай сходим'")
    #
    # # event_title = page_title[i].find_all('a', class_='impression-card-title')
    # # event_price_location_date = soup.find_all('div', 'impression-card-info')
    #
    #     for i in range(len(event_title)):
    #         print(event_title[i].text)
    #         print('Больше информации: ')
    #         print(event_price_location_date[i].text)
    #         if i != (len(event_title)-1):
    #             print('Следующее событие: ')
