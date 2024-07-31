def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]

def inspect_salary_from(vacancy: dict) -> int:
    """обрабатывает заработную плату"""
    if vacancy["salary"] is None:
        return 0
    from_salary = vacancy["salary"]["from"]
    to_salary = vacancy["salary"]["to"]
    if vacancy['salary']['currency'] != "RUR":
        return 0
    elif from_salary and to_salary:
        return int(from_salary)
    elif to_salary is None:
        return 0
    elif from_salary is None:
        return 0




