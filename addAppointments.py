import core
import datetime
import os

dictAppointments = {"data":[]}

def loadInfoAppointments():
    global dictAppointments
    if core.checkFile("appointments.json"):
        dictAppointments = core.loadInfo("appointments.json")
    else:
        core.crearInfo("appointments.json", dictAppointments)

def createAppointment():
    isRunning = True
    while isRunning:
        os.system("clear")
        print("Ingrese los datos de la cita")
        try:
            name = validateName()
            date = validateDate()
            time = validateTime()
            reason = validateReason()

            data = {
                'namePatient': name,
                'date': date.strftime("%d/%m/%Y"),
                'time': time.strftime("%H:%M"),
                'reason': reason
            }

            core.crearInfo("appointments.json", data)
            dictAppointments["data"].append(data)
            print("Cita agregada correctamente")
            input("Presione enter para continuar")
            isRunning = False
        except ValueError:
            print("Ingrese un valor valido")
            input("Presione enter para continuar")

def validateName():
    while True:
        try:
            os.system("clear")
            name = input("Ingrese el nombre del paciente: ").upper()
            if name == "":
                print("Ingrese un nombre valido")
            else:
                return name
        except ValueError:
            print("Ingrese un nombre valido")

def validateDate():
    while True:
        os.system("clear")
        date_str = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
        try:
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            if date < datetime.datetime.now():
                print("No puede ingresar una fecha pasada")
            else:
                return date
        except ValueError:
            print("Ingrese una fecha valida")

def validateTime():
    while True:
        os.system("clear")
        print("Horario de atención:")
        print(" - Mañana: 08:00 - 12:00")
        print(" - Tarde: 14:00 - 18:00")
        print("")
        time_str = input("Ingrese la hora de la cita (hh:mm): ")
        try:
            if time_str < "08:00" or time_str > "18:00":
                print("Ingrese una hora valida")
            elif time_str > "12:00" and time_str < "14:00":
                print("Ingrese una hora valida")
            else:
                time = datetime.datetime.strptime(time_str, "%H:%M")
                return time
        except ValueError:
            print("Ingrese una hora valida")

def validateReason():
    while True:
        try:
            os.system("clear")
            reason = input("Ingrese la razon de la cita: ")
            if reason == "":
                print("Ingrese una razon valida")
            else:
                return reason
        except ValueError:
            print("Ingrese una razon valida")
        