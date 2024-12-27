# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'

    try:
        patients = admin.load_patients()
        print('Loaded patients from file.')
    except FileNotFoundError:
        patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('David','Smith', 15, '07123456789','C1 ABC')]
        print('No patients found in file, using default data.')

    doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'),Doctor('Jone', 'Carlos', 'Cardiology')]
    discharged_patients = []

    # Add symptoms to patients
    # if patients:
    #     patients[0].add_symptom('Cough')
    #     patients[0].add_symptom('Fever')
    #     patients[1].add_symptom('Headache')
    #     patients[2].add_symptom('Sore throat')




    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print()
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- View doctor\'s assigned patients')
        print(' 7- View patient\'s assigned doctor')
        print(' 8- View patient\'s symptoms')
        print(' 9- Add symptom to patient')
        print(' 10- Group patients by Surname')
        print(' 11- Relocate patient to another doctor')
        print(' 12- View management report')
        print(' 13- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)


        elif op == '2':
            # 2- View or discharge patients
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)


                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            # View patients assigned to each doctor
            for doctor in doctors:
                doctor.view_assigned_patients()

        elif op == '7':
            # 7- View doctor's assigned patients
            for patient in patients:
                patient.view_assigned_doctor()


        elif op == '8':
            # 8- View patient symptoms
            admin.view_patient_symptoms(patients)

        elif op == '9':
            # 9- Add symptom to patient
            admin.add_symptom_to_patient(patients)

        elif op == '10':
            # 9- Group patients by Surname
            admin.group_patients_by_surname(patients)

        elif op == '11':
            # 11- Relocate patient to another doctor
            admin.relocate_patient(patients, doctors)

        elif op == '12':
            # 12- View management report
            admin.view_management_report(patients, doctors, discharged_patients)

        elif op == '13':
            # 13- Quit
            admin.save_patients(patients)
            running = False


        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
