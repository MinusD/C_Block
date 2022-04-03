"""
Создать класс Hospital.
    Поля:
        + название больницы,
        + адрес,
        + список врачей (список экземпляров класса Doctor),
        + список медсестер (список экземпляров класса Nurse)

    Определить конструктор.

    Переопределить метод
        преобразования в строку для печати всей информации о больнице (с использованием
        переопределения в классах Doctor и Nurse).

    Переопределить методы
        + получения количества врачей функцией len,
        + получения врача по индексу,
        изменения по индексу,
        удаления по индексу (пусть номера врачей считаются с 1, а индекс 0 – список всех медсестер).

    Переопределить операции + и - для добавления или удаления врача.
    Добавить функцию создания txt-файла и записи всей информации в него
    (в том числе пациентов врачей и графика работы медсестер).
"""
import traceback
from Nurse import Nurse
from Doctor import Doctor


class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.doctors = []
        self.nurses = []

    def __str__(self):
        print(321)

    def __add__(self, doc):
        self.doctors.append(doc)

    def __len__(self):
        return len(self.doctors)

    def __getitem__(self, i):
        try:
            return self.doctors[i - 1] if i else self.nurses
        except IndexError:
            print("Something wrong! Doctor not found!")


if __name__ == '__main__':
    try:
        hos = Hospital('Центральная больница #1', 'Волоколамское ш., 84, Москва, 125424')
        doc = Doctor("Вова", "Медвен", 35, 10, "Окулист")
        hos + doc
        print(len(hos))
        print(hos[0])
        print(hos[1])
        print(hos[2])


    except AssertionError:
        print("TEST ERROR")
        traceback.print_exc()
    else:
        print("TEST PASSED")
