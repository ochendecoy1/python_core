# Создайте программу, имитирующую работу клиники. Создайте базовый
# класс Doctor с методом treat(). От него создайте три дочерних класса:
# Surgeon, Dentist и Therapist. В каждом дочернем классе
# переопределите метод treat(), чтобы каждый врач выводил сообщение
# о своём способе лечения.
# Создайте класс Patient, содержащий атрибуты treatment_plan — код
# плана лечения и doctor — назначенный пациенту врач. В классе
# Therapist реализуйте метод назначения врача пациенту. Если код плана
# лечения равен 1, пациенту назначается хирург; если код равен 2 —
# дантист; при любом другом значении — терапевт.
# После назначения врача необходимо сохранить соответствующий объект
# врача в patient.doctor и вызвать у него метод treat(). Создайте
# пациента, задайте ему план лечения и продемонстрируйте работу
# программы.

class Doctor:
    def treat(self):
        print("Доктор проводит лечение (базовая реализация).")


class Surgeon(Doctor):
    def treat(self):
        print("Хирург: провожу операцию.")


class Dentist(Doctor):
    def treat(self):
        print("Дантист: лечу зуб.")


class Therapist(Doctor):
    # это в интернете подглядел, чтобы упростить вызов
    @staticmethod
    def assign_doctor(patient):
        if patient.treatment_plan == 1:
            patient.doctor = Surgeon()
            print(f"Назначен хирург (план {patient.treatment_plan}).")
        elif patient.treatment_plan == 2:
            patient.doctor = Dentist()
            print(f"Назначен дантист (план {patient.treatment_plan}).")
        else:
            patient.doctor = Therapist()
            print(f"Назначен терапевт (план {patient.treatment_plan}).")

        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None  # по умолчанию без врача


p1 = Patient(treatment_plan=1)
print("--- Пациент 1 ---")
Therapist.assign_doctor(p1)

p2 = Patient(treatment_plan=2)
print("\n--- Пациент 2 ---")
Therapist.assign_doctor(p2)

p3 = Patient(treatment_plan=3)
print("\n--- Пациент 3 ---")
Therapist.assign_doctor(p3)