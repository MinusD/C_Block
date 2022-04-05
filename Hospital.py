"""
Создать класс Hospital.
    Поля:
        + название больницы,
        + адрес,
        + список врачей (список экземпляров класса Doctor),
        + список медсестер (список экземпляров класса Nurse)

    + Определить конструктор.

    Переопределить метод
        + преобразования в строку для печати всей информации о больнице (с использованием
        + переопределения в классах Doctor и Nurse).

    Переопределить методы
        + получения количества врачей функцией len,
        + получения врача по индексу,
        + изменения по индексу,
        + удаления по индексу (пусть номера врачей считаются с 1, а индекс 0 – список всех медсестер).

    + Переопределить операции + и - для добавления или удаления врача.
    + Добавить функцию создания txt-файла и записи всей информации в него
    + (в том числе пациентов врачей и графика работы медсестер).
"""
import traceback
from Nurse import Nurse
from Doctor import Doctor


class Hospital:
    def __init__(self, name, address, doctors=[], nurses=[]):
        self.name = name
        self.address = address
        self.doctors = doctors
        self.nurses = nurses

    def __str__(self):
        a = f'Название больницы: {self.name}\nАдрес: {self.address}\n\nДоктора:\n'
        for i in range(len(self.doctors)):
            a += (self.doctors[i].__str__() + '\n\n')
        a += "Медсёстры:\n"
        for i in range(len(self.nurses)):
            a += (self.nurses[i].__str__() + '\n\n')

        return a

    def __add__(self, doc):
        self.doctors.append(doc)

    def __len__(self):
        return len(self.doctors)

    def __getitem__(self, i):
        try:
            return self.doctors[i - 1] if i else self.nurses
        except IndexError:
            print("Something wrong! Doctor not found!")

    def __setitem__(self, key, data):
        try:
            if key:
                self.doctors[key - 1] = data
            else:
                self.nurses = data
        except IndexError:
            print("Something wrong! Doctor not found!")

    def __delitem__(self, key):
        try:
            if key:
                del self.doctors[key - 1]
            else:
                del self.nurses
        except IndexError:
            print("Something wrong! Doctor not found!")

    def __sub__(self, other):
        for i in range(len(self.doctors)):
            if self.doctors[i] == other:
                del self.doctors[i]

    def make_txt(self, filename='HospitalData.txt'):
        with open(filename, 'w') as f:
            f.write(f'Название больницы: {self.name}\nАдрес: {self.address}\n\nДоктора:\n')
            for i in range(len(self.doctors)):
                f.write('----------\n' + self.doctors[i].__str__() + '\nПациенты:\nID    | Surname N.P.\n')
                for key, value in self.doctors[i].patients.items():
                    f.write('{: <5}'.format(key))
                    f.write(' | ')
                    f.write('{: <5}'.format(value))
                    f.write('\n')
            f.write('\nМедсёстры:\n')
            for i in range(len(self.nurses)):
                f.write('----------\n' + self.nurses[i].__str__() + '\nРасписание:\n')
                for key, value in self.nurses[i].schedule.items():
                    f.write('{: <7}'.format(key))
                    f.write(' | ')
                    f.write('{: <5}'.format(value))
                    f.write('\n')


if __name__ == '__main__':
    try:
        nurse = Nurse("Анна", "Анимова", 20, 234, "Центральный департамент",
                        {'Monday': '10:00-17:00', 'Tuesday': '10:00-17:00', 'Friday': '10:00-17:00'})
        hos = Hospital('Центральная больница #1', 'Волоколамское ш., 84, Москва, 125424', [], [nurse])
        doc = Doctor("Вова", "Медве", 35, 10, "Окулист")
        doc.new_patient(1, "Petrov F.E.")
        doc.new_patient(2, "Voronov V.R.")
        doc.new_patient(3, "Repotrov S.P.")
        doc2 = Doctor("Андрей", "Ашарев", 26, 15, "Хирург")
        doc3 = Doctor("Матвей", "Дерентев", 24, 15, "Терапевт")

        hos + doc
        hos + doc2
        print(hos)
        print(len(hos))
        print(hos[0])
        print(hos[1])
        print(hos[3])
        print(hos)
        hos.make_txt()
        hos[1] = doc3
        del hos[2]
        print(hos)

    except AssertionError:
        print("TEST ERROR")
        traceback.print_exc()
    else:
        print("TEST PASSED")
