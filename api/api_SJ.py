import requests
from api.api import API
from vacancie import Vacancie

class SuperJobAPI(API):
    def __init__(self):
       pass

    def connect(self):
        # Connect to the SuperJob API

        '''
        Метод `connect()` делает запрос API,
        используя библиотеку `requests`.
        Ответ от API возвращается в виде объекта JSON
        '''

        params = {
            'keyword': 'Python'
        }
        headers = {
            'X-Api-App-Id': 'v3.h.4496946.a4de17e42d306b1d0cd5ea6ff54597dc93771b3a.b067604f53dbe9997179663d5fd85029dd0199bc'
        }

        try:
            req = requests.get('https://api.superjob.ru/2.0/vacancies', headers=headers, params=params)
            req.raise_for_status()  # Raise an exception if the request was unsuccessful
            return req.json()
        except requests.exceptions.RequestException as e:

            print(f"An error occurred: {e}")
            return None

    def match_keyword(self, vacancy, keyword):
        return keyword.lower() in vacancy['profession'].lower()


    def get_vacancies(self):

        # Get job vacancies from the SuperJob API

        response = self.connect()
        if response is None:
            return []

        items = response['objects']
        vacancies = []

        for item in items:
            name = item['profession']
            area = item['place_of_work']['title']
            address = item['address']
            salary_from = item['payment_from']
            salary_to = item['payment_to']
            experience = item['experience']['title']

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
#
if __name__ == '__main__':
    superjob_api = SuperJobAPI()
    # print(superjob_api.connect())
    print(superjob_api.get_vacancies())