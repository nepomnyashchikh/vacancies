import requests
from api.api import API
from vacancie import Vacancie


class HeadHunterAPI(API):

    def __init__(self):
        '''
        Параметры для поиска вакансий
        '''
        self.search_params = None
        self.__area = None
        self.__experience = None
        self.__currency = None
        self.__only_with_salary = False
        self.__salary = None
        self.__page = 0
        self.__per_page = 100

    def connect(self):
        # Connect to the HeadHunter API
        params = {"text": self.search_params,
                    "experience": self.__experience,
                    "area": self.__area,
                    "only_with_salary": self.__only_with_salary,
                    "currency": self.__currency,
                    "salary": self.__salary,
                    "page": self.__page,
                    "per_page": self.__per_page
                }
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def match_keyword(self, vacancy, keyword):
        return keyword.lower() in vacancy['name'].lower()

    def get_vacancies(self):
        # Get job vacancies from the HeadHunter API
        items = self.connect().get('items', [])
        vacancies = []

        for counter, item in enumerate(items, start=1):
            name = item['name']
            area = item['area']['name']
            address = item['address'].get('raw') if item['address'] else None
            salary_from = item['salary'].get('from') if item['salary'] else None
            salary_to = item['salary'].get('to') if item['salary'] else None
            experience = item['experience']['name']

            vacancy = Vacancie(name, area, address, salary_from, salary_to, experience)
            vacancies.append(vacancy)

            print(
                f'Вакансия: {name}\n',
                f'местоположение: {area}\n',
                f'адрес: {address}\n',
                f'зарплата {salary_from} - {salary_to}\n',
                f'опыт: {experience}\n',
            )


        return vacancies


if __name__ == '__main__':
    aka = HeadHunterAPI()

    print(aka.get_vacancies())