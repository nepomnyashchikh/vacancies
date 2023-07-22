from abc import ABC, abstractmethod


class API(ABC):
    '''
       Абстрактный класс для работы с api
       сайтов с вакансиями
       '''
    @abstractmethod
    def get_vacancies(self):
        '''
        Возвращает список вакансий
        '''
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def match_keyword(self):
        pass
