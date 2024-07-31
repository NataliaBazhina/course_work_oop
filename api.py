from abc import ABC, abstractmethod
import requests

from src.JSONsaver import JSONsaver
from src.utils import inspect_salary_from
from src.vacancies import Vacancy


class Parser(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """Получает вакансии"""
        pass

class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 1}
        self.vacancies = []
        self.json_saver = JSONsaver('file.json')



    def get_vacancies(self, keyword):

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            for vacancy in vacancies:
                salary = inspect_salary_from(vacancy)
                vacancy = Vacancy(vacancy['name'], vacancy['alternate_url'], salary, vacancy['snippet']['responsibility'], vacancy['snippet']['requirement'])
                self.json_saver.add_vacancy(vacancy)
                self.vacancies.extend(vacancies)
                self.params['page'] += 1




