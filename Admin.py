from Doctor import Doctor

from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index + 1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        print("-----Login-----")
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if self.__username == username and self.__password == password:
            print("Login successful!")
            return self.__username
        else:
            raise Exception("Invalid Credentials")

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False

    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and speciality of the doctor in that order.
        """
        first_name = input("Enter the doctor's first name: ")
        surname = input("Enter the doctor's surname: ")
        speciality = input("Enter the doctor's speciality: ")
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')



        op = input('Input: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()
            #ToDo4
            pass

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break

                if not name_exists:
                    new_doctor = Doctor(first_name, surname, speciality)
                    doctors.append(new_doctor)
                    print('Doctor registered.')
                    break

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            update_op = int(input('Input: ')) # make the user input lowercase

            if update_op == 1:
                new_first_name = input('Enter the new first name: ')
                doctors.set_first_name(index,new_first_name)

            elif update_op == 2:
                new_surname = input('Enter the new surname: ')
                doctors.set_surname(index,new_surname)

            elif update_op == 3:
                new_speciality = input('Enter the new speciality: ')
                doctors.set_speciality(index,new_speciality)
            else:
                print('Invalid Option!')

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
            try:
                doctor_index = input('Enter the ID of the doctor to be deleted: ')
                if doctor_index!=False:
                    doctors.pop(doctor_index)
                    print('Doctot deleted')
                else:
                    print('Doctor not found')
            except ValueError:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation chosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')

        for index, patient in enumerate(patients): print(f'{index + 1:3}|{patient}')

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return

        except ValueError:
            print('The id entered is incorrect')
            return

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                doctors[doctor_index].add_patient(patients[patient_index])
                patients[patient_index].link(doctors[doctor_index].full_name())
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1

            if self.find_index(patient_index, patients):
                discharge_patients.append(patients.pop(patient_index))
                print('Patient discharged.')
            else:
                print('Patient not found.')
        except ValueError: \
            print('The ID entered is incorrect')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, patient in enumerate(discharged_patients): print(f'{index + 1:3}|{patient}')

    def update_details(self):
        """
        Allows the user to update and change username, password, and address
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            new_username = input('Enter the new username: ')
            self.__username = new_username
            print('Username updated successfully.')

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print('Password updated successfully.')
            else:
                print('Passwords do not match. Please try again.')

        elif op == 3:
            new_address = input('Enter the new address: ')
            self.__address = new_address
            print('Address updated successfully.')

        else:
            print('Invalid option.')


