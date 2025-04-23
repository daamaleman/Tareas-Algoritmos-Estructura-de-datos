
import models.patient_model as pm

# Agrega un nuevo paciente a la lista
def add_patient(queue, name, age, symptom, priority):
    patient = pm.Patient(name, age, symptom, priority)
    queue.append(patient)

# Muestra todos los pacientes en la lista
def show_queue(queue):
    if not queue:
        print("No hay pacientes en espera.")
        return
    print("\nLista de pacientes en orden de llegada:")
    for idx, patient in enumerate(queue, 1):
        print(f"{idx}. {patient.name} | Edad: {patient.age} | Síntoma: {patient.symptom} | Prioridad: {patient.priority}")

# Atiende al siguiente paciente (el primero en la lista)
def attend_patient(queue):
    if not queue:
        print("No hay pacientes para atender.")
        return
    patient = queue.pop(0)
    print(f"Paciente atendido: {patient.name} con síntoma: {patient.symptom}")
