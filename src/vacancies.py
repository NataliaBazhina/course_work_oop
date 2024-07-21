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

{
    "items": [
        {
            "id": "101503409",
            "premium": false,
            "name": "IT Intern",
            "department": null,
            "has_test": false,
            "response_letter_required": false,
            "area": {
                "id": "2759",
                "name": "Ташкент",
                "url": "https://api.hh.ru/areas/2759"
            },
            "salary": null,
            "type": {
                "id": "open",
                "name": "Открытая"
            },
            "address": null,
            "response_url": null,
            "sort_point_distance": null,
            "published_at": "2024-07-15T14:22:00+0300",
            "created_at": "2024-07-15T14:22:00+0300",
            "archived": false,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=101503409",
            "show_logo_in_search": null,
            "insider_interview": null,
            "url": "https://api.hh.ru/vacancies/101503409?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/101503409",
            "relations": [],
            "employer": {
                "id": "10486823",
                "name": "Центр развития IT- знаний",
                "url": "https://api.hh.ru/employers/10486823",
                "alternate_url": "https://hh.ru/employer/10486823",
                "logo_urls": {
                    "90": "https://img.hhcdn.ru/employer-logo/6536893.png",
                    "240": "https://img.hhcdn.ru/employer-logo/6536894.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1229113.png"
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10486823",
                "accredited_it_employer": false,
                "trusted": true
            },
            "snippet": {
                "requirement": "Knowledge of English at an advanced level. Willingness to learn and grow in technology and programming.",
                "responsibility": "Basic knowledge in IT field. Participating in the design and creation of innovative solutions to improve user; experience and enhance..."
            },
            "contacts": null,
            "schedule": {
                "id": "fullDay",
                "name": "Полный день"
            },
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": false,
            "professional_roles": [
                {
                    "id": "40",
                    "name": "Другое"
                }
            ],
            "accept_incomplete_resumes": true,
            "experience": {
                "id": "noExperience",
                "name": "Нет опыта"
            },
            "employment": {
                "id": "full",
                "name": "Полная занятость"
            },
            "adv_response_url": null,
            "is_adv_vacancy": false,
            "adv_context": null
        }
    ],
    "found": 13021,
    "pages": 2000,
    "page": 0,
    "per_page": 1,
    "clusters": null,
    "arguments": null,
    "fixes": null,
    "suggests": null,
    "alternate_url": "https://hh.ru/search/vacancy?enable_snippets=true&items_on_page=1&text=python"
}