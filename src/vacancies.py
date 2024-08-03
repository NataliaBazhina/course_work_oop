
class Vacancy:
    """Класс для представления информации о вакансии."""

    def __init__(self, title:str, link:str, salary:int, description:str, requirements:str):
        """ метод инициализации объекта вакансии"""
        self.title = self._validate_title(title)
        self.link = self._validate_link(link)
        self.salary = self._validate_salary(salary)
        self.description = self._validate_description(description)
        self.requirements = self._validate_requirements(requirements)

    def _validate_title(self, title: str) -> str:
        """метод валидации названия вакансии"""
        if not title or not isinstance(title, str):
            raise ValueError("Заголовок вакансии должен быть непустой строкой.")
        return title

    def _validate_link(self, link: str) -> str:
        """метод валидации ссылки"""
        if not link or not isinstance(link, str):
            raise ValueError("Ссылка должна быть непустой строкой.")
        return link

    def _validate_salary(self, salary: int) -> int:
        """метод валидации зарплаты"""
        if not isinstance(salary, int) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным целым числом.")
        return salary

    def _validate_description(self, description: str) -> str:
        """метод валидации описания вакансии"""
        if not isinstance(description, str):
            raise ValueError("Описание должно быть строкой.")
        return description

    def _validate_requirements(self, requirements: str) -> str:
        """метод валидации требований к вакансии"""
        if not isinstance(requirements, str):
            raise ValueError("Требования должны быть строкой.")
        return requirements


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



