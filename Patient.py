class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = []

    def full_name(self):
        """Full name is first_name and surname"""
        return f'{self.__first_name} {self.__surname}'

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        """Args: doctor (string): the doctor full name"""
        self.__doctor = doctor

    def add_symptom(self, symptom):
        """Adds a symptom to the list of symptoms"""
        self.__symptoms.append(symptom)

    def print_symptoms(self):
        """Prints all the symptoms"""
        if self.__symptoms:
            print(f'Symptoms of {self.full_name()}:')
            for symptom in self.__symptoms:
                print(f'- {symptom}')
        else:
            print(f'{self.full_name()} has no symptoms listed.')

    def view_assigned_doctor(self):
        """Prints the assigned doctor's full name"""
        print(f'The assigned doctor is: {self.__doctor}')

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'

    def to_dict(self):
        """
        Convert patient object to dictionary
        """
        return {
            'first_name': self.__first_name,
            'surname': self.__surname,
            'age': self.__age,
            'mobile': self.__mobile,
            'postcode': self.__postcode,
            'doctor': self.__doctor,
            'symptoms': self.__symptoms
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a patient object from dictionary
        """

        patient = cls(data['first_name'], data['surname'], data['age'], data['mobile'], data['postcode'])
        patient.__doctor = data['doctor']
        patient.__symptoms = data['symptoms']

        return patient

    def surname(self):
        """
        Return the surname of the patient
        """
        return self.__surname
