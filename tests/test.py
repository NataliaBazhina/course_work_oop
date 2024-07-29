import pytest
from src.vacancies import Vacancy
def test_compare():
    vacancy = Vacancy("Программист", "http://example.com/job1", 60000, "Разработка приложений на Python",
                      "Опыт работы 2 года")
    vacancy1 = Vacancy("Аналитик", "http://example.com/job2", 50000, "Анализ данных", "Знание SQL")
    assert vacancy > vacancy1
    assert vacancy != vacancy1

