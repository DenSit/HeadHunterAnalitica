import os
from key_skills import Extractor
from pagination import LoadPages
from extract_vacancies import LoadVacancies


class Requirements:
    def __init__(self, vacancy):
        self.vacancy = vacancy
        self.folder_pagination = './docs/pagination/'
        self.folder_vacancies = './docs/vacancies/'

    def get_vacancies(self):
        self.cleaner()
        print(" Идёт загрузка вакансий, пожалуйста подождите ...")
        LoadPages(self.folder_pagination, self.vacancy).pagination()
        print(" Идёт извлечение ключевых навыков, пожалуйста подождите ...")
        LoadVacancies(self.folder_pagination, self.folder_vacancies).get_vacancies()
        Extractor(self.folder_vacancies, self.vacancy).extract_key_skills()
        print("Ключевые навыки извлечены, подсчитаны, отсортированны в порядке убывания и записаны в файл "
              f"'{self.vacancy}.txt' ")

    def cleaner(self):
        for folder in (self.folder_pagination, self.folder_vacancies):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')


if __name__ == "__main__":
    key_skills = Requirements('Python developer')
    key_skills.get_vacancies()
