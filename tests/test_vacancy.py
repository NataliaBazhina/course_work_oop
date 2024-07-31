import pytest
from src.vacancies import Vacancy


class TestVacancy:

    @pytest.fixture
    def setup_vacancies(self):
        """создание экземпляров класса Vacancy"""

        vacancy1 = Vacancy("Программист", "http://example.com/vacancy1", 100000, "Описание вакансии 1", "Требования 1")
        vacancy2 = Vacancy("Аналитик", "http://example.com/vacancy2", 80000, "Описание вакансии 2", "Требования 2")
        vacancy3 = Vacancy("Менеджер", "http://example.com/vacancy3", None, "Описание вакансии 3", "Требования 3")
        return vacancy1, vacancy2, vacancy3

    def test_vacancy_initialization(self, setup_vacancies):
        """ метод проверки инициализации объектов Vacancy"""
        vacancy1, _, _ = setup_vacancies


        assert vacancy1.title == "Программист"
        assert vacancy1.link == "http://example.com/vacancy1"
        assert vacancy1.salary == 100000
        assert vacancy1.description == "Описание вакансии 1"
        assert vacancy1.requirements == "Требования 1"

    def test_vacancy_salary_default(self, setup_vacancies):
        """ метод проверки вакансий, где зарплата не указана"""
        _, _, vacancy3 = setup_vacancies

        assert vacancy3.salary == "Зарплата не указана"

    def test_vacancy_equality(self, setup_vacancies):
        """ метод проверки сравнения на равенство"""
        vacancy1, vacancy2, _ = setup_vacancies

        assert vacancy1 == Vacancy("Разработчик", "http://example.com/vacancy4", 100000, "Описание вакансии 4",
                                   "Требования 4")
        assert vacancy1 != vacancy2
    #
    def test_vacancy_less_than(self, setup_vacancies):
        """ проверка на меньшую зарплату"""
        vacancy1, vacancy2, _ = setup_vacancies

        assert vacancy2 < vacancy1

    def test_vacancy_str(self, setup_vacancies):
        """ проверка на строковое представление вакансии"""
        vacancy1, _, _ = setup_vacancies

        expected_str = "Vacancy(title=Программист, link=http://example.com/vacancy1, salary=100000, description=Описание вакансии 1, requirements=Требования 1)"
        assert str(vacancy1) == expected_str




if __name__ == "__main__":
    pytest.main()