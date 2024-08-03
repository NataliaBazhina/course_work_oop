
def get_top_vacancies(sorted_vacancies, top_n):
    """ выдает топ-вакансии"""
    return sorted_vacancies[:top_n]

def inspect_title(vacancy: dict) -> str:
    """Проверяет и возвращает заголовок вакансии."""
    return vacancy.get("name", "")

def inspect_link(vacancy: dict) -> str:
    """Проверяет и возвращает ссылку на вакансию."""
    return vacancy.get("alternate_url", "")

def inspect_salary_from(vacancy: dict):
    """обрабатывает заработную плату"""
    if vacancy["salary"] is None:
        return 0
    if isinstance(vacancy["salary"], int):
        return vacancy["salary"]
    if isinstance(vacancy["salary"], str):
        if vacancy["salary"].lower() in ['зарплата не указана', 'не указана']:
            return 0

        cleaned_salary = vacancy["salary"].replace(' ', '').replace('руб.', '').replace('руб', '')
        try:
            return int(cleaned_salary)
        except ValueError:
            return 0
    if isinstance(vacancy["salary"], dict):
        salary_from = vacancy["salary"].get('from')
        salary_to = vacancy["salary"].get('to')
        if salary_from and salary_to:
            return (salary_from + salary_to) // 2
        return salary_from if salary_from else salary_to if salary_to else 0
    return 0

def inspect_description(vacancy: dict) -> str:
    """Проверяет и возвращает описание вакансии."""
    if vacancy.get("snippet", {}).get("responsibility", "") is None:
        return ""
    else:
        return vacancy.get("snippet", {}).get("responsibility", "")

def inspect_requirements(vacancy: dict) -> str:
    """Проверяет и возвращает требования вакансии."""
    return vacancy.get("snippet", {}).get("requirement", "")





