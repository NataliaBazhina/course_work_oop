from abc import ABC, abstractmethod
import requests
from src.JSONsaver import JSONsaver
from src.utils import inspect_salary_from, inspect_title, inspect_link, inspect_description, inspect_requirements
from src.vacancies import Vacancy


class Parser(ABC):
    """
    Абстрактный класс для работы с API
    """
    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """абстрактный метод для получения вакансии"""
        pass

class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """метод для инициализации объекта класса HH """
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 1}
        self.vacancies = []
        self.json_saver = JSONsaver('file.json')



    def get_vacancies(self, keyword):
        """ метод для получения вакансий"""

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.__url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            for vacancy in vacancies:
                title = inspect_title(vacancy)
                link = inspect_link(vacancy)
                description = inspect_description(vacancy)
                requirements = inspect_requirements(vacancy)
                salary = inspect_salary_from(vacancy)
                vacancy = Vacancy(title, link, salary, description, requirements)
                self.json_saver.add_vacancy(vacancy)
                self.vacancies.extend(vacancies)
                self.params['page'] += 1




