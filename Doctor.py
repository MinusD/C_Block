from Person import Person


class Doctor(Person):
    def __init__(self, name, surname, age, id_number, speciality):
        Person.__init__(self, name, surname, age)
        self.id_number = name
        self.speciality = speciality
        self.patients = {}

    def new_patient(self, patient_id, patient_sn):
        self.patients[patient_id] = patient_sn

    def kill_patient(self, patient_id):
        try:
            self.patients.pop(patient_id)
        except:
            print(f"Somthing wrong! Failed to delete patient with id {patient_id}!")

    def all_patient(self):
        print("ID    | Surname N.P.   ")
        for key, value in self.patients.items():
            print('{: <5}'.format(key), end=" | ")
            print('{: <5}'.format(value))

    def __str__(self):
        return f'ФИ: {self.surname} {self.name}\nВозраст: {self.age}\nНомер удосоверения: {self.id_number}\nСпециальность: {self.speciality}'
