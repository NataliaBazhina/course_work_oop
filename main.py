from api import HH
from src.utils import get_top_vacancies
from src.JSONsaver import JSONsaver


def user_interaction():
    hh = HH()
    json_saver = JSONsaver('file.json')

    while True:
        print("\nМеню:")
        print("1. Ввести поисковый запрос для вакансий")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            try:
                keyword = input("Введите название вакансии: ")
                vacancies = hh.get_vacancies(keyword)
            except ValueError:
                print("Некорректный ввод. Попробуйте еще раз.")


        elif choice == '2':
            salary = input('Введите диапазон зарплат через "-":').split('-')
            n = int(input("Введите количество вакансий для вывода в топ N: "))
            filtered_vacancies = sorted(json_saver.get_vacancies_by_salary(salary),reverse=True)
            top_vacancies = get_top_vacancies(filtered_vacancies,n)
            for vacancy in top_vacancies:
                print(vacancy)
        elif choice == '3':
            keyword = input("Введите ключевые слова для фильтрации вакансий: ")
            filtered_vacancies = json_saver.get_vacancies_by_keywords(keyword)
            for vacancy in filtered_vacancies:
                print(vacancy['title'])

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")





if __name__ == "__main__":
    user_interaction()