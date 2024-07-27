from src.vacancies import Vacancy
def test_compare():
    vac = Vacancy("IT Intern", "ghj", 50, "gjkm", "hjn")
    vac1 = Vacancy("hjh", "hjhgf",30, "jhf", "bfg")
    assert vac > vac1
    assert vac != vac1
