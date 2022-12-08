from application.salary import  calculate_salary
from application.db.people import get_employees
import datetime






if __name__ == '__main__':
    cal_sar = calculate_salary(16000, 10, 21)
    сreat_people = get_employees('Alex', 'Ionov')
    now = datetime.datetime.now()
    print(now)