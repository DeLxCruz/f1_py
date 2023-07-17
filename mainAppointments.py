import os
import addAppointments
import searchAppointments
import editAppointments
import removeAppointments


if __name__: "__main__"
isRunning = True
while isRunning:
    os.system("clear")
    os.system("pause")
    os.system("clear")
    print("+","-"*43,"+")
    print("|{:10}{:10}{:10}|".format("", "GESTIÓN DE CITAS CAMPUSMD", "", "", "", "", ""))
    print("+","-"*43,"+")
    print("|{:^15}{:^10}{:^15}|".format("", "1. Agregar cita", "", ""))
    print("+","-"*43,"+")
    print("|{:^15}{:^10}{:^16}|".format("", "2. Buscar cita", "", ""))
    print("+","-"*43,"+")
    print("|{:^15}{:^10}{:^16}|".format("", "3. Editar cita", "", ""))
    print("+","-"*43,"+")
    print("|{:^15}{:^10}{:^14}|".format("", "4. Eliminar cita", "", ""))
    print("+","-"*43,"+")
    print("|{:^15}{:^8}{:^22}|".format("", "5. Salir", "", ""))
    print("+","-"*43,"+")
    try:
        option = int(input("Ingrese una opcion: "))
        if option == 1:
            addAppointments.loadInfoAppointments()
            addAppointments.createAppointment()
        elif option == 2:
            searchAppointments.loadInfoAppointments()
            searchAppointments.searchAppointment()
        elif option == 3:
            editAppointments.loadInfoAppointments()
            editAppointments.editAppointment()
        elif option == 4:
            removeAppointments.loadInfoAppointments()
            removeAppointments.removeAppointment()
        elif option == 5:
            isRunning = False
            print("Gracias por usar el programa :D")
            print("Vuelva pronto")
        else:
            print('')
            print("Ingrese una opcion valida")
    except ValueError:
        print('')
        print("Ingrese una opcion valida")
        input("Presione enter para continuar")