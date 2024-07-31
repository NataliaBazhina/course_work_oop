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

# def inspect_salary_from(vacancy: dict) -> int:
#         """Парсинг зарплаты из строки"""
#     if salary is None:
#         return 0
#     if isinstance(salary, int):
#         return salary
#     if isinstance(salary, str):
#         if salary.lower() in ['зарплата не указана','не указана']:
#             return 0
#
#         cleaned_salary = salary.replace(' ','').replace('руб.', '').replace('руб', '')
#         try:
#             return int(cleaned_salary)
#         except ValueError:
#             return 0
#     if isinstance(salary, dict):
#         salary_from = salary.get('from')
#         salary_to = salary.get('to')
#         if salary_from and salary_to:
#             return (salary_from + salary_to) // 2
#         return salary_from if salary_from else salary_to if salary_to else 0
#     return 0


