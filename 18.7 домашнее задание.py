import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
        5. Вывести все оценки определенного ученика
        6. Вывести средний балл по каждому предмету по определенному ученику
        7. Удаление предмета из базы данных
        8. Удаление ученика из базы данных
        9. Изменение имени ученика
        10. Изменение названия предмета
        11. Изменение оценки ученика
        12. Удаление оценки ученика
        13. Заведение нового предмета в журнал
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Выход из программы')
        break
    elif command == 5:
        print('5. Вывести все оценки определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print('ОШИБКА: Неверно указано имя ученика')
    elif command == 6:
        print('6. Вывести средний балл по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
                print()
        else:
            print('ОШИБКА: Неверно указано имя ученика')
    elif command == 7:
        print('7. Удаление предмета из базы данных')
        class_ = input('Введите название предмета, который нужно удалить: ')
        if class_ in classes:
            classes.remove(class_)
            print('Предмет удален')
            print(f'Список предметов: {classes}')
        else:
            print('ОШИБКА: Указанного предмета нет в списке')
    elif command == 8:
        print('8. Удаление ученика из базы данных')
        name = input('Введите имя ученика, которое нужно удалить: ')
        if name in students:
            students.remove(name)
            print('Ученик удален из базы данных')
            print(f'Список учеников: {students}')
        else:
            print('ОШИБКА: Указанного students нет в списке')
    elif command == 9:
        print('9. Изменение имени ученика')
        print(students)
        old_name = input('Введите имя ученика для редактирования: ')
        if old_name in students:
            new_name = input('Введите новое имя ученика: ')
            index = students.index(old_name)
            students[index] = new_name
            print('Имя изменено')
            print(students)
        else:
            print('ОШИБКА: Указанного ученика нет в списке')
    elif command == 10:
        print('10. Изменение названия предмета')
        print(classes)
        old_class = input('Введите название предмета для редактирования: ')
        if old_class in classes:
            new_class = input('Введите новое название предмета: ')
            index = classes.index(old_class)
            classes[index] = new_class
            print('Название изменено')
            print(classes)
        else:
            print('ОШИБКА: Указанного предмета нет в списке')
    elif command == 11:
        print('11. Изменение оценки ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            subject = input('Введите название предмета, в котором хотите исправить оценку: ')
            if subject in students_marks[student]:
                marks = students_marks[student][subject]
                print(f"Оценки ученика {student} по предмету '{subject}' : {marks}")
                old_mark = int(input('Укажите очередность оценки, которую хотите исправить: '))
                if 1 <= old_mark <= len(marks):
                    new_mark = int(input('Введите новую оценку от 1 до 5: '))
                    if 1 <= new_mark <= 5:
                        marks[old_mark - 1] = new_mark
                        print('Оценка исправлена!')
                        print(f"Оценки ученика {student} по предмету '{subject}' : {marks}")
                    else:
                        print('Оценка должна быть от 1 до 5!')
                else:
                    print('Указанного номера оценки не существует')
            else:
                print('ОШИБКА: Указанного предмета нет в журнале')
        else:
            print('ОШИБКА: Указанного ученика нет в списке')
    elif command == 12:
        print('12. Удаление оценки ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            subject = input('Введите название предмета, в котором необходимо удалить оценку: ')
            if subject in students_marks[student]:
                marks = students_marks[student][subject]
                print(f"Оценки ученика {student} по предмету '{subject}' : {marks}")
                old_mark = int(input('Введите очередность оценки, которую хотите удалить: '))
                if 1 <= old_mark <= len(marks):
                    del_mark = marks.pop(old_mark - 1)
                    print(f'Оценка {old_mark} удалена!')
                    print(f"Оставшиеся оценки: {marks}")
                else:
                    print('Указанного номера оценки не существует')
            else:
                print('ОШИБКА: Указанного предмета нет в журнале')
        else:
            print('ОШИБКА: Указанного ученика нет в списке')
    elif command == 13:
        print('13. Заведение нового предмета в журнал')
        new_classes = input('Введите новый предмет: ')
        if new_classes not in classes:
            classes.append(new_classes)
            for student in students_marks:
                students_marks[student][new_classes] = []
            print(f'Предмет "{new_classes}" успешно добавлен!')
            print('Текущий список предметов:', classes)
        else:
            print('Данный предмет уже есть в журнале')
