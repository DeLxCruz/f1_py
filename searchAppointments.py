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

def searchAppointment():
    isRunning = True
    while isRunning:
        os.system("clear")
        print("+","-"*35,"+")
        print("|{:13}{:15}{:9}|".format("", "BUSCAR CITA", "", "", "", "", ""))
        print("+","-"*35,"+")
        print("|{:^5}{:^10}{:^6}|".format("", "[N] Buscar cita por nombre", "", ""))
        print("+","-"*35,"+")
        print("|{:^5}{:^10}{:^7}|".format("", "[F] Buscar cita por fecha", "", ""))
        print("+","-"*35,"+")
        print("|{:^5}{:^10}{:^4}|".format("", "[V] Volver al menu principal", "", ""))
        print("+","-"*35,"+")
        print("")
        try:
            option = input("Ingrese una opcion: ").upper()
            if option == "N":
                searchByName()
                isRunning = False
            elif option == "F":
                searchByDate()
                isRunning = False
            elif option == "V":
                isRunning = False
            else:
                print("")
                print("Ingrese una opcion valida")
                input("Presione enter para continuar")
        except ValueError:
            print("")
            print("Ingrese una opcion valida")
            input("Presione enter para continuar")

def searchByName():
    isRunning = True
    while isRunning:
        os.system("clear")
        print("BÚSQUEDA CITAS POR NOMBRE")
        try:
            name = input("Ingrese el nombre del paciente: ").upper()
            nameFound = False
            if name == "":
                print("")
                print("El nombre no puede estar vacio")
                input("Presione enter para continuar")
                isRunning = False
            elif name.isdigit():
                print("")
                print("El nombre no puede ser un numero")
                input("Presione enter para continuar")
                isRunning = False
            else:
                os.system("clear")
                print("+","-"*81,"+")
                print("|{:30}{:25}{:28}|".format("", "CITAS ENCONTRADAS", "", "", "", "", ""))
                print("+","-"*81,"+")
                print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Nombre del paciente", "Fecha de la cita", "Hora de la cita", "Razon de la cita"))
                print("+","-"*81,"+")
                for appointment in dictAppointments["data"]:
                    if name in appointment["namePatient"]:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(appointment["namePatient"], appointment["date"], appointment["time"], appointment["reason"]))
                        print("+","-"*81,"+")
                        nameFound = True
                        isRunning = False
                if not nameFound:
                    print("")
                    print("No se encontraron citas con ese nombre")
                    isRunning = False
                print("")
                input("Presione enter para continuar")
        except ValueError:
            print("")
            print("Ingrese un nombre valido")
            input("Presione enter para continuar")

def searchByDate():
    isRunning = True
    while isRunning:
        os.system("clear")
        print("BÚSQUEDA CITAS POR FECHA")
        try:
            date_str = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
            dateFound = False
            if date_str == "":
                print("")
                print("La fecha no puede estar vacia")
                input("Presione enter para continuar")
                isRunning = False
            else:
                date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
                os.system("clear")
                print("+","-"*81,"+")
                print("|{:30}{:25}{:28}|".format("", "CITAS ENCONTRADAS", "", "", "", "", ""))
                print("+","-"*81,"+")
                print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Nombre del paciente", "Fecha de la cita", "Hora de la cita", "Razon de la cita"))
                print("+","-"*81,"+")
                for appointment in dictAppointments["data"]:
                    if date.strftime("%d/%m/%Y") in appointment["date"]:
                        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(appointment["namePatient"], appointment["date"], appointment["time"], appointment["reason"]))
                        print("+","-"*81,"+")
                        dateFound = True
                        isRunning = False
                if not dateFound:
                    print("")
                    print("No se encontraron citas con esa fecha")
                    isRunning = False
                print("")
                input("Presione enter para continuar")
        except ValueError:
            print("")
            print("Ingrese una fecha valida")
            input("Presione enter para continuar")
