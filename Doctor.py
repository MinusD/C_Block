import traceback
from Person import Person


class Doctor(Person):
    def __init__(self, name, surname, age, id_number, speciality):
        Person.__init__(self, name, surname, age)
        self.id_number = id_number
        self.speciality = speciality
        self.patients = {}

    def new_patient(self, patient_id, patient_sn):
        self.patients[patient_id] = patient_sn

    def del_patient(self, patient_id):
        try:
            self.patients.pop(patient_id)
        except:
            print(f"Something wrong! Failed to delete patient with id {patient_id}!")

    def all_patient(self):
        print("ID    | Surname N.P.")
        for key, value in self.patients.items():
            print('{: <5}'.format(key), end=" | ")
            print('{: <5}'.format(value))

    def __str__(self):
        return f'ФИ: {self.surname} {self.name}\nВозраст: {self.age}\nНомер удостоверения: {self.id_number}' \
               f'\nСпециальность: {self.speciality}'


if __name__ == '__main__':
    try:
        doc = Doctor("Vova", "Medven", 35, 10, "Proctologist")
        doc.new_patient(1, "Petrov F.E.")
        doc.new_patient(2, "Voronov V.R.")
        doc.new_patient(3, "Repotrov S.P.")
        doc.all_patient()
        doc.del_patient(2)
        doc.del_patient(2)
        doc.all_patient()
        print(doc)
    except AssertionError:
        print("TEST ERROR")
        traceback.print_exc()
    else:
        print("TEST PASSED")
