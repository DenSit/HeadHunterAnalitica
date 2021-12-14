import requests
import json
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
            jsObj = json.loads(self.getPage(page))
            nextFileName = f'{self.pagination_folder}{page}.json'
            with open(nextFileName, mode='w', encoding='utf8') as f:
                f.write(json.dumps(jsObj, ensure_ascii=False))
                t = random.randint(1, 100)
                time.sleep(0.01 * t)

    def getPage(self, page=0):
        params = {
            'text': f'NAME:{self.vacancy}',
            'area': 1,
            'page': page,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        return data


