import json
import os
import requests
import random
import time


class LoadVacancies:

    def __init__(self, folder_pagination, folder_vacancies):
        self.folder_pagination = folder_pagination
        self.folder_vacancies = folder_vacancies

    def get_vacancies(self):
        animation = ["    *", "    **", "    ***", "    ****", "    *****", "    ******", "          "]
        i = 0
        for file in os.listdir(self.folder_pagination):
            f = open(f'{self.folder_pagination}{file}', encoding='utf-8')
            jsonObj = json.loads(f.read())
            f.close()
            try:
                for v in jsonObj['items']:
                    print(animation[i % len(animation)], end="\r")
                    i += 1
                    req = requests.get(v['url'])
                    data = req.content.decode()
                    req.close()
                    fileName = f'{self.folder_vacancies}{v["id"]}.json'
                    f = open(fileName, mode='w', encoding='utf8')
                    f.write(data)
                    f.close()
                    t = random.randint(1, 10)
                    time.sleep(0.01 * t)
            except KeyError:
                pass


