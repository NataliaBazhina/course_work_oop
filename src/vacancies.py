import json

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



    def save_vacancies(self):
        """ сохраняет вакансии в файл """
        with open(self.file_path, 'w', encoding="utf-8") as f:
            json.dump(self.vacancies, f, ensure_ascii=False, indent=4)




# hh = HH()
# hh.get_vacancies("python")
# print(hh.vacancies)

