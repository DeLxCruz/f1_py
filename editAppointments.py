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

def editAppointment():
    isRunning = True
    while isRunning:
        os.system("clear")
        print("EDITAR CITAS")
        print('')  
        print('LISTA DE CITAS')
        print('')
        try:
            for i,j in enumerate(dictAppointments["data"]):
                print(f'{i + 1}. Nombre del Paciente: {j["namePatient"]}')
            print('')
            appointmentSelected = int(input("Seleccione una cita o presione para volver al menú: "))
            appointmentSelected -= 1

            if 0 <= appointmentSelected < len(dictAppointments["data"]):
                showSelected = dictAppointments["data"][appointmentSelected]
                os.system("clear")
                print('Cita seleccionada:')
                print(f'- Nombre del paciente: {showSelected["namePatient"]} - Fecha de la cita: {showSelected["date"]} - Hora de la cita: {showSelected["time"]} - Razon de la cita: {showSelected["reason"]}')

                print('')
                newDate_str = input("Ingrese la nueva fecha de la cita (dd/mm/aaaa): ")
                print('')
                newHour_str = input("Ingrese la nueva hora de la cita (hh:mm): ")

                try:
                    newDate = datetime.datetime.strptime(newDate_str, "%d/%m/%Y").strftime("%d/%m/%Y")
                    newHour = datetime.datetime.strptime(newHour_str, "%H:%M").strftime("%H:%M")

                    dictAppointments["data"][appointmentSelected]["date"] = newDate
                    dictAppointments["data"][appointmentSelected]["time"] = newHour

                    editAppointment = dictAppointments["data"][appointmentSelected]
                    print("La cita se ha modificado correctamente")
                    input("Presione enter para continuar")
                    os.system("clear")
                    print('Cita modificada:')
                    print('')
                    print(f'- Nombre del paciente: {editAppointment["namePatient"]} - Fecha de la cita: {editAppointment["date"]} - Hora de la cita: {editAppointment["time"]} - Razon de la cita: {editAppointment["reason"]}')

                    core.editarData("appointments.json", dictAppointments)
                    input("Presione enter para continuar")
                    isRunning = False
                except ValueError:
                    print("Ingrese una fecha valida")
                    input("Presione enter para continuar")
            else:
                print("Ingrese una opcion valida")
                input("Presione enter para continuar")
        except ValueError:
            print("Está saliendo del programa")
            input("Presione enter para continuar")
            isRunning = False