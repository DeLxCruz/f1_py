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

def removeAppointment():
    isRunning = True
    while isRunning:
        os.system("clear")
        print("ELIMINAR CITAS")
        print('')
        print('LISTA DE CITAS:')
        print('')
        try:
            for i,j in enumerate(dictAppointments["data"]):
                print(f'{i + 1}. Nombre del Paciente: {j["namePatient"]} - Fecha de la cita: {j["date"]} - Hora de la cita: {j["time"]}')
            print('')
            appointmentSelected = int(input("Seleccione una cita o presione enter para volver al menú: "))
            appointmentSelected -= 1

            if 0 <= appointmentSelected < len(dictAppointments["data"]):
                showSelected = dictAppointments["data"][appointmentSelected]
                os.system("clear")
                print('Cita seleccionada:')
                print('')
                print(f'- Nombre del paciente: {showSelected["namePatient"]} - Fecha de la cita: {showSelected["date"]} - Hora de la cita: {showSelected["time"]} - Razon de la cita: {showSelected["reason"]}')
                print('')
                confirm = input("¿Esta seguro que desea eliminar esta cita? (S/N): ").upper()
                if confirm == "S":
                    dictAppointments["data"].pop(appointmentSelected)
                    print("La cita se ha eliminado correctamente")
                    input("Presione enter para continuar")
                    core.editarData("appointments.json", dictAppointments)
                    isRunning = False
                elif confirm == "N":
                    isRunning = False
                else:
                    print("Ingrese una opcion valida")
                    input("Presione enter para continuar")
            else:
                print("Ingrese una opcion valida")
                input("Presione enter para continuar")
        except ValueError:
            print("Está saliendo del programa")
            input("Presione enter para continuar")
            isRunning = False