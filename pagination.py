import requests
import time
import random


class LoadPages:
    """
    getting response from api HH (pages) in json
    """
    def __init__(self, pagination_folder, vacancy):
        self.pagination_folder = pagination_folder
        self.vacancy = vacancy

    def pagination(self):
        for page in range(0, 10):
            with open(f'{self.pagination_folder}{page}.json', mode='w', encoding='utf8') as f:
                f.write(self.getPage(page))
                time.sleep(0.01 * random.randint(1, 10))

    def getPage(self, page=0):
        params = {
            'text': f'NAME:{self.vacancy}',
            'area': 1,
            'page': page,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        return req.text


