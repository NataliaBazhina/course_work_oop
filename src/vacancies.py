import requests
from abc import ABC, abstractmethod
class Parser(ABC):
    """Абстрактный класс для работы с вакансиями."""

    @abstractmethod
    def load_vacancies(self,keyword):
        pass

    import requests

class HH(Parser):
        """
        Класс для работы с API HeadHunter
        Класс Parser является родительским классом, который вам необходимо реализовать
        """

        def __init__(self, file_worker):
            self.url = 'https://api.hh.ru/vacancies'
            self.headers = {'User-Agent': 'HH-User-Agent'}
            self.params = {'text': '', 'page': 0, 'per_page': 100}
            self.vacancies = []
            super().__init__(file_worker)

        def load_vacancies(self, keyword):
            self.params['text'] = keyword
            while self.params.get('page') != 20:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1


    # @abstractmethod
    # def get_vacancies(self):
    #     """Получает вакансии"""
    #
    #
    # @abstractmethod
    # def save_vacancies_to_file(self, vacancies, filename):
    #     """Сохраняет вакансии в файл"""
    #
    #
    # @abstractmethod
    # def load_vacancies_from_file(self, filename, criteria=None):
    #     """Загружает список вакансий из файла по заданным критериям."""
    #
    #
    # @abstractmethod
    # def delete_vacancies_from_file(self, filename, criteria=None):
    #     """Удаляет информацию о вакансиях из файла по заданным критериям."""



class HhVacancy(Vacancy):
    """Класс для работы с API HeadHunter."""

    def init(self, api):
        self.api = api

    def get_vacancies(self):
        """Получает список вакансий"""

    def save_vacancies_to_file(self, vacancies, filename):
        """Сохраняет список вакансий в JSON-файл."""




    def delete_vacancies_from_file(self, filename, criteria):
        """Удаляет информацию о вакансиях из JSON-файла по заданным критериям."""


class VacancyInfo:
    """Класс для представления информации о вакансии."""

    def init(self, title, link, salary, description, requirements):
        self.title = title
        self.link = link
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.requirements = requirements

