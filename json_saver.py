import json
import os.path
from abc import ABC, abstractmethod
from api.api_HH import HeadHunterAPI
from api.api_SJ import SuperJobAPI



class VacancyStorage(ABC):
    @abstractmethod
    def select(self, keyword):
        pass

    @abstractmethod
    def insert(self, vacancy):
        pass

    @abstractmethod
    def delete(self, keyword):
        pass


class JsonSaver(VacancyStorage):
    def __init__(self, path):
        self.path = path
        self.connect()

    def connect(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file:
                file.write(json.dumps([]))

    def select(self, keyword):
        self.keyword = keyword
        # поиск по keyword в файле

    def insert(self, vacancy):
        vacancy_json = vacancy.to_json()
        with open(self.path, "a") as file:
            file.write(json.dumps(vacancy_json) + '\n')

    def match_keyword(self, vacancy, keyword):
        if keyword.lower() in vacancy['title'].lower() or keyword.lower() in vacancy['description'].lower():
            return True
        else:
            return False

    def delete(self, keyword):
        temp_file_path = self.path + '.temp'
        with open(self.path, "r") as file, open(temp_file_path, "w") as temp_file:
            for line in file:
                vacancy = json.loads(line)
                if not self.match_keyword(vacancy, keyword):
                    temp_file.write(line)
        os.replace(temp_file_path, self.path)


if __name__ == '__main__':
    storage = JsonSaver('TEST_jsonSaver.json')

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies()
    for vacancy in hh_vacancies:
        storage.insert(vacancy)

    sj_api = SuperJobAPI()
    sj_vacancies = sj_api.get_vacancies()
    for vacancy in sj_vacancies:
        storage.insert(vacancy)