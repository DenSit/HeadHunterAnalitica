import json
import os
import operator


class Extractor:
    """
    extracting key skills, counting, sorting and writing in file
    """
    def __init__(self, folder, name_vacancy=''):
        self.key_skills = {}
        self.folder = folder
        self.name = name_vacancy

    def extract_key_skills(self):
        for fl in os.listdir(self.folder):
            with open(f'{self.folder}{fl}', encoding='utf-8') as file:
                jsonObj = json.loads(file.read())
                try:
                    for key in jsonObj['key_skills']:
                        self.key_skills[key["name"]] = self.key_skills.get(key["name"], 0) + 1
                except KeyError:
                    pass
        return self.sorted_extract_skills(self.key_skills)

    def sorted_extract_skills(self, skills):
        sorted_key_skills = sorted(skills.items(), key=operator.itemgetter(1))
        with open(f"{self.name}.txt", 'w') as f:
            f.write(f"Ключевые наыки по вакансии {self.name}: " + '\n')
            n = 1
            for key in sorted_key_skills[::-1]:
                space = 71 if n < 10 else 70
                f.write(str(n) + ". " + key[0] + " " + "_" * (space - len(key[0])) + str(key[1]) + "\n")
                n += 1


if __name__ == "__main__":
    obj = Extractor('./docs/vacancies/', 'Аналитик')
    obj.extract_key_skills()

