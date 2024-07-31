from api import HH
def test_get_vacancies():
    hh_parser = HH()
    hh_parser.get_vacancies('Software Engineer')
    assert len(hh_parser.vacancies) > 0, "Должно быть найдено хотя бы одно объявление о вакансии"
    for vacancy in hh_parser.vacancies:
        assert 'Software Engineer' or 'Помощник главного инженера' in vacancy['name'], "Название вакансии должно содержать ключевое слово"
    assert hh_parser.params['page'] > 0, "Количество страниц должно увеличиться после запроса"


