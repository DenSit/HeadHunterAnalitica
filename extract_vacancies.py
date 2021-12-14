import json
import os
import requests
import random
import time


class LoadVacancies:
    """
    obtaining vacancies, which lay in pages
    """
    def __init__(self, folder_pagination, folder_vacancies):
        self.folder_pagination = folder_pagination
        self.folder_vacancies = folder_vacancies

    def get_vacancies(self):
        animation = ["    *", "    **", "    ***", "    ****", "    *****", "    ******", "          "]
        i = 0
        for file in os.listdir(self.folder_pagination):
            with open(f'{self.folder_pagination}{file}', encoding='utf-8') as f:
                jsonObj = json.loads(f.read())
                try:
                    for v in jsonObj['items']:
                        print(animation[i % len(animation)], end="\r")  # animation in command line
                        i += 1
                        fileName = f'{self.folder_vacancies}{v["id"]}.json'
                        with open(fileName, mode='w', encoding='utf8') as file:
                            file.write(requests.get(v['url']).text)
                        time.sleep(0.01 * random.randint(1, 10))
                except KeyError:
                    print('ERROR')


if __name__ == '__main__':
    x = LoadVacancies('./docs/pagination/', './docs/vacancies/')
    x.get_vacancies()
