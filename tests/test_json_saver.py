import pytest
import os
import json
from src.vacancies import Vacancy
from src.JSONsaver import JSONsaver

TEST_FILE_PATH = "test_vacancies.json"


@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown():
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)
    yield
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)


def test_add_vacancy(setup_and_teardown):
    """метод проверки добавления вакансий в файл"""

    saver = JSONsaver(TEST_FILE_PATH)
    vacancy = Vacancy("Software Engineer", "http://example.com", 100000, "Develop cool software", "Python, Django")
    saver.add_vacancy(vacancy)
    with open(TEST_FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]['title'] == "Software Engineer"
        assert data[0]['link'] == "http://example.com"
        assert data[0]['salary'] == 100000
        assert data[0]['description'] == "Develop cool software"
        assert data[0]['requirements'] == "Python, Django"

def test_delete_vacancy(setup_and_teardown):
    """ метод проверки удаления вакансии из файла"""

    saver = JSONsaver(TEST_FILE_PATH)
    vacancy = Vacancy("Software Engineer", "http://example.com", 100000, "Develop cool software", "Python, Django")
    saver.add_vacancy(vacancy)
    saver.delete_vacancy("Software Engineer")
    with open(TEST_FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 0
#
#

