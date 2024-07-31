from abc import ABC, abstractmethod
import json
from json import JSONDecodeError
from src.vacancies import Vacancy
import os
from src.utils import get_top_vacancies

class Saver(ABC):
    """Абстрактный класс для работы с файлом"""
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_keywords(self, keywords):
        pass

    @abstractmethod
    def delete_vacancy(self, title):
        pass

class JSONsaver(Saver):

    def __init__(self,file_path):
        self.file_path = file_path
        self.vacancies = self._load_vacancies()

    def add_vacancy(self, vacancy: Vacancy):
        """добавляет вакансию в файл"""
        vac = {
            "title": vacancy.title,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "description": vacancy.description,
            "requirements": vacancy.requirements
        }
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding="utf-8") as f:
                json.dump([], f)
        self.vacancies.append(vac)
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(self.vacancies, f, ensure_ascii=False, indent=4)
        print(f"Вакансия '{vacancy.title}'добавлена")


    def delete_vacancy(self, title):
        """Удаляет вакансию с указанным заголовком из файла"""
        if not os.path.exists(self.file_path):
            print("Файл не найден.")
            return
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy["title"] != title]
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(self.vacancies, f, ensure_ascii=False, indent=4)
        print(f"Вакансия '{title}' удалена из файла.")


    def get_vacancies_by_keywords(self, keywords):
        """Отбирает вакансии по ключевым словам в описании"""
        filtered_vacancies = []
        for vacancy in self.vacancies:
            if 'description' in vacancy and vacancy['description']:
                description = vacancy['description'].lower()
                for word in keywords.split():
                    if word in description:
                        filtered_vacancies.append(vacancy)
                        break
        return filtered_vacancies

    def get_vacancies_by_salary(self, salary_range):
        start,stop = salary_range
        filtered_vacancies = []
        for vacancy in self.vacancies:
            try:
                salary = int(vacancy['salary'])
            except ValueError:
                salary = 0
            if int(start) <= salary <= int(stop):
                vacancy = Vacancy(vacancy['title'], vacancy['link'], vacancy['salary'], vacancy['description'], vacancy['requirements'])
                filtered_vacancies.append(vacancy)
        return filtered_vacancies



    def _load_vacancies(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                if data is not None:
                    return data
                else:
                    return []
        except FileNotFoundError:
            return []
        except JSONDecodeError:
            return []


# jsonsaver = JSONsaver("file_path.json")
# vacancy = Vacancy("Программист","http://example.com/job1",60000,"Разработка приложений на Python","Опыт работы 2 года")
# vacancy1 = Vacancy("Аналитик", "http://example.com/job2", 50000, "Анализ данных", "Знание SQL")
# vacancy2 = Vacancy("Дизайнер", "http://example.com/job3", 55000, "Дизайн интерфейсов", "Навыки работы с Figma")

# jsonsaver.add_vacancy(vacancy)
# jsonsaver.add_vacancy(vacancy1)
# #
# jsonsaver.delete_vacancy("Аналитик")
# jsonsaver.add_vacancy(vacancy2)
#
# vacancies = [vacancy, vacancy1, vacancy2]
# keyword = "интерфейс"
# filtered_vacancies = jsonsaver.get_vacancies_by_keywords(keyword)
# print("Отфильтрованные вакансии:")
# for vacancy in filtered_vacancies:
#     print(vacancy['title'])

# salary = (30000, 100000)
# filtered_vacancies = sorted(jsonsaver.get_vacancies_by_salary(salary),reverse=True)
# print(len(filtered_vacancies))
# top_vacancies = get_top_vacancies(filtered_vacancies,3)
# print(len(top_vacancies))
# print("Отфильтрованные вакансии:")
# for vacancy in top_vacancies:
#     print(vacancy.title, vacancy.salary)


