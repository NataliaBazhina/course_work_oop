import pytest
from src.vacancies import Vacancy

def test_valid_initialization():
    """Тест успешной инициализации объекта Vacancy с корректными параметрами."""
    vacancy = Vacancy(
        title="Программист",
        link="http://example.com/vacancy",
        salary=100000,
        description="Работа с Python",
        requirements="Знание Python, опыт работы."
    )
    assert vacancy.title == "Программист"
    assert vacancy.link == "http://example.com/vacancy"
    assert vacancy.salary == 100000
    assert vacancy.description == "Работа с Python"
    assert vacancy.requirements == "Знание Python, опыт работы."


@pytest.mark.parametrize("title", [
    "",                   # пустая строка
    123,                 # не строка
    0,                   #ноль
])
def test_invalid_title(title):
    """Тест на недопустимый заголовок вакансии."""
    with pytest.raises(ValueError, match="Заголовок вакансии должен быть непустой строкой."):
        Vacancy(title=title, link="http://example.com", salary=100000, description="Тест", requirements="Тест")


@pytest.mark.parametrize("link", [
    "",                   # пустая строка
    123,                 # не строка
])
def test_invalid_link(link):
    """Тест на недопустимую ссылку вакансии."""
    with pytest.raises(ValueError, match="Ссылка должна быть непустой строкой."):
        Vacancy(title="Тест", link=link, salary=100000, description="Тест", requirements="Тест")


@pytest.mark.parametrize("salary", [
    -1000,               # отрицательное число
    "100023",            # не целое число
])
def test_invalid_salary(salary):
    """Тест на недопустимую зарплату вакансии."""
    with pytest.raises(ValueError, match="Зарплата должна быть неотрицательным целым числом."):
        Vacancy(title="Тест", link="http://example.com", salary=salary, description="Тест", requirements="Тест")


@pytest.mark.parametrize("description", [
    12345,                # не строка
])
def test_invalid_description(description):
    """Тест на недопустимое описание вакансии."""
    with pytest.raises(ValueError, match="Описание должно быть строкой."):
        Vacancy(title="Тест", link="http://example.com", salary=100000, description=description, requirements="Тест")


@pytest.mark.parametrize("requirements", [
    12345,                # не строка
])
def test_invalid_requirements(requirements):
    """Тест на недопустимые требования к кандидату."""
    with pytest.raises(ValueError, match="Требования должны быть строкой."):
        Vacancy(title="Тест", link="http://example.com", salary=100000, description="Тест", requirements=requirements)


def test_equality():
    """Тест метода равенства (==)."""
    vacancy1 = Vacancy("Программист", "http://example.com/1", 100000, "Описание", "Требования")
    vacancy2 = Vacancy("Системный администратор", "http://example.com/2", 100000, "Описание", "Требования")
    assert vacancy1 == vacancy2


def test_less_than():
    """Тест метода сравнения <."""
    vacancy1 = Vacancy("Программист", "http://example.com/1", 80000, "Описание", "Требования")
    vacancy2 = Vacancy("Системный администратор", "http://example.com/2", 100000, "Описание", "Требования")
    assert vacancy1 < vacancy2


def test_str():
    """Тест метода строкового представления объекта."""
    vacancy = Vacancy("Программист", "http://example.com", 100000, "Работа с Python", "Знание Python")
    assert str(vacancy) == "Vacancy(title=Программист, link=http://example.com, salary=100000, description=Работа с Python, requirements=Знание Python)"


if __name__ == "__main__":
    pytest.main()