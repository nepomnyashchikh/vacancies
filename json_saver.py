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
            with open(self.path, 'w', encoding='utf-8') as file:
                file.write(json.dumps([]))
    def select(self, keyword):
        self.keyword = keyword

    def insert(self, vacancy):
        vacancy_json = vacancy.to_json()
        with open(self.path, "a", encoding='utf-8') as file:
            file.write(json.dumps(vacancy_json, ensure_ascii=False) + '\n')

    def match_keyword(self, vacancy, keyword):
        if keyword.lower() in vacancy['title'].lower() or keyword.lower() in vacancy['description'].lower():
            return True
        else:
            return False

    def delete(self, keyword):
        temp_file_path = self.path + '.temp'
        with open(self.path, "r", encoding='utf-8') as file, open(temp_file_path, "w", encoding='utf-8') as temp_file:
            for line in file:
                vacancy = json.loads(line)
                if not self.match_keyword(vacancy, keyword):
                    temp_file.write(line)
        os.replace(temp_file_path, self.path)

class CustomHeadHunterAPI(HeadHunterAPI):
    def match_keyword(self, vacancy, keyword):
        pass

class CustomSuperJobAPI(SuperJobAPI):
    def match_keyword(self, vacancy, keyword):
        pass


if __name__ == '__main__':
    storage = JsonSaver('TEST_jsonSaver.json')

    hh_api = CustomHeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies()
    for vacancy in hh_vacancies:
        storage.insert(vacancy)

    sj_api = CustomSuperJobAPI()
    sj_vacancies = sj_api.get_vacancies()
    for vacancy in sj_vacancies:
        storage.insert(vacancy)