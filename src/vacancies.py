from abc import ABC, abstractmethod
from api import HH
import json
import os

class Vacancy:
    """Класс для представления информации о вакансии."""

    def __init__(self, title:str, link:str, salary:int, description:str, requirements:str):
        self.title = title
        self.link = link
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.requirements = requirements

    def __eq__(self, other):
        """ метод сравнения вакансий с равной зарплатой"""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False

    def __lt__(self, other):
        """ метод сравнения вакансий с меньшей зарплатой"""
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return False

    def __str__(self):
        """Представление информации о вакансии в виде строки."""
        return f"Vacancy(title={self.title}, link={self.link}, salary={self.salary}, description={self.description}, requirements={self.requirements})"

    def add_vacancy(self,file_path):
        """добавляет вакансию в файл"""
        vac = {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description,
            "requirements": self.requirements
        }
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding="utf-8") as f:
                json.dump([], f)
        with open(file_path, 'r', encoding="utf-8") as f:
            vacancies = json.load(f)
        vacancies.append(vac)
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(vacancies, f, indent=4)
        print(f"Вакансия добавлена") #добавить название вакансии!

    def delete_vacancy(self, file_path, title):
            """Удаляет вакансию с указанным заголовком из файла"""
            if not os.path.exists(file_path):
                print("Файл не найден.")
                return
            with open(file_path, 'r', encoding="utf-8") as f:
                vacancies = json.load(f)
            vacancies = [vacancy for vacancy in vacancies if vacancy["title"] != title]

            with open(file_path, 'w', encoding="utf-8") as f:
                json.dump(vacancies, f, indent=4)
            print(f"Вакансия '{title}' удалена из файла.")

    def get_vacancies_by_criteria(vacancies, criteria):
        """отбирает вакансии по ключевым словам в описании"""
        return [v for v in vacancies if v.description and any(word in v.description.lower() for word in criteria)]

    # def save_vacancies(self):
    #     """ сохраняет вакансии в файл """
    #     with open(self.file_path, 'w', encoding="utf-8") as f:
    #         json.dump(self.vacancies, f, indent=4)


class VacancyFile(ABC):
    """Класс для работы с файлом"""
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_criteria(self, filename,criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

# hh = HH()
# hh.get_vacancies("python")
# print(hh.vacancies)

vacancy = Vacancy("jgg","hjn",12,"jhg","jg")
vacancy1 = Vacancy("jhhgf","kyf",60, "hg","jgf")
vacancy2 = Vacancy("khg","jg",90,"khg","jgfg")
vacancy.add_vacancy("kjm.json")
vacancy1.add_vacancy("kjm.json")
vacancy2.add_vacancy("kjm.json")
vacancy2.delete_vacancy("kjm.json","khg")

