import json
from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """Получает вакансии"""
        pass

class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 1}
        self.vacancies = []

    def save_vacancies(self):
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(self.vacancies, f, indent=4)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

hh = HH("vac.json")
hh.load_vacancies("python")
hh.save_vacancies()
print(hh.vacancies)