from api.api_HH import HeadHunterAPI
from api.api_SJ import SuperJobAPI
from json_saver import JsonSaver


class InteractivePlatform:
    def __init__(self):
        self.api_hh = HeadHunterAPI()
        self.api_sj = SuperJobAPI()
        self.storage = JsonSaver('vacancies.json')

    def start(self):
        while True:
            try:
                print("Выберите платформу для поиска вакансий:")
                print("1. HeadHunter")
                print("2. SuperJob")
                print("3. Выход")

                choice = input("Введите номер платформы: ")

                if choice == "1":
                    self.search_vacancies(self.api_hh)
                elif choice == "2":
                    self.search_vacancies(self.api_sj)
                elif choice == "3":
                    break
                else:
                    print("Некорректный выбор. Попробуйте снова.")
            except ValueError:
                print('Вы указали неверное значение!')

    def search_vacancies(self, api):
        keyword = input("Введите ключевое слово для поиска: ")
        city = input("Введите город (для всех введите '-'): ")
        salary = input("Введите зарплату (для любой введите '-'): ")
        experience = input("Введите требуемый опыт работы (для любого введите '-'): ")

        api.search_params = keyword
        api.area = city
        api.salary = salary
        api.experience = experience

        vacancies = api.get_vacancies()

        if len(vacancies) == 0:
            print("По заданным параметрам не найдено вакансий")
        else:
            print(f"Найдено {len(vacancies)} вакансий:")
            for vacancy in vacancies:
                print(vacancy)

                # Сохраняем вакансию в хранилище
                self.storage.insert(vacancy)

    def run(self):
        self.start()