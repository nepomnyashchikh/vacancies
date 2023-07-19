class Vacancie:
    def __init__(self, name, area, address, salary_from, salary_to, experience):
        self.name = name
        self.area = area
        self.address = address
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.experience = experience

    def validate_salary(self):
        # Валидация зарплаты
        if self.salary_from and (not isinstance(self.salary_from, (int, float)) or self.salary_from < 0):
            raise ValueError("Зарплата 'от' должна быть числом, больше или равной нулю.")
        if self.salary_to and (not isinstance(self.salary_to, (int, float)) or self.salary_to < 0):
            raise ValueError("Зарплата 'до' должна быть числом, больше или равной нулю.")

    def __str__(self):
        return f"Вакансия: {self.name}\nРегион: {self.area}\nАдрес: {self.address}\nЗарплата от: {self.salary_from}\nЗарплата до: {self.salary_to}\nТребуемый опыт работы: {self.experience}"

    def __eq__(self, other):
        # Сравнение вакансий по зарплате 'от'
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        # Сравнение вакансий по зарплате 'от'
        return self.salary_from < other.salary_from

    def to_json(self):
        return {
            'name': self.name,
            'area': self.area,
            'address': self.address,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'experience': self.experience
        }