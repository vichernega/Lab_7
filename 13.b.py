#Чернеги Вікторії   Б19_д/122Б
#Програма виводить на екран користувача дані про працівників (прізвище, рік народження, посаду, зарплатню та освіту)

while True:

    persons = {'per1': 'Smith', 'per2': 'Johnson', 'per3': 'Brown', 'per4': 'Jones'}
    birthdays = {'y1': '1989', 'y2': '1978', 'y3': '1999', 'y4': '1992'}
    positions = {'pos1': 'Chemical Engineer', 'pos2': 'Computer Engineer', 'pos3': 'Drafting and Design Engineer',
                 'pos4': 'Automotive Engineer'}
    salaries = {'sa1': '15390', 'sa2': '23478', 'sa3': '16789', 'sa4': '20456'}
    educations = {'e1': 'VNTU', 'e2': 'DONNU', 'e3': 'DONNU', 'e4': 'KPI'}

    per_values, year_values, pos_values, sal_values, ed_values = list(persons.values()), list(birthdays.values()), list(
        positions.values()), list(salaries.values()), list(educations.values())

    for per, year, pos, sal, ed in zip(per_values, year_values, pos_values, sal_values, ed_values):
        print(f'Surname: {per};   Birthday: {year};   Position: {pos};   Salary: {sal};   Education: {ed}')


    answer = input('Restart? Yes - 1. No - other.')
    if answer == '1':
        continue
    else:
        break