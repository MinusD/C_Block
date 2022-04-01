"""
Создать производный от Person класс Nurse. Новые поля: номер удостоверения, отделение работы, график работы
    (словарь вида день недели: часы работы). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения отделения, добавления, удаления и изменения графика работы. Переопределить
    метод преобразования в строку для печати основной информации (ФИ, возраст, номер удостоверения, отделение).
"""
from Person import Person


class Nurse(Person):
    def __init__(self, name, surname, age, id_number, department, schedule):
        Person.__init__(self, name, surname, age)
        self.id_number = id_number
        self.department = department
        self.schedule = schedule
        '''days_data = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(len(schedule)):
            self.schedule.update({days_data[i]: schedule[i]})'''

    def edit_department(self, department):
        self.department = department

    def add_schedule(self, day, time):
        if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            self.schedule.update({day: time})
        else:
            print("Something wrong! Failed to add schedule.")

    def delete_schedule(self, day):
        if day in self.schedule.keys():
            self.schedule.pop(day)
        else:
            print("Something wrong! Failed to delete schedule.")

    def edit_schedule(self, day, time):
        if day in self.schedule.keys():
            self.schedule.update({day: time})
        else:
            print("Something wrong! Failed to edit schedule.")

    def __str__(self):
        return f'ФИ: {self.surname} {self.name}\nВозраст: {self.age}\nНомер удостоверения: {self.id_number}' \
               f'\nОтделение: {self.department}'
