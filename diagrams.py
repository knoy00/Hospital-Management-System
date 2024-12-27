import matplotlib.pyplot as plt

# Example data
doctors = ['Dr. John Smith', 'Dr. Jone Smith', 'Dr. Jone Carlos']
patients_per_doctor = [5, 3, 7]
appointments_per_doctor = [10, 8, 12]
illness_types = ['Cough', 'Fever', 'Headache']
patients_per_illness = [4, 5, 6]

def plot_total_doctors():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.bar(['Doctors'], [len(doctors)], color='blue')
    ax.set_xlabel('Total Doctors')
    ax.set_ylabel('Count')
    ax.set_title('Total Number of Doctors in the System')
    return fig

def plot_bar_chart_patients():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(doctors, patients_per_doctor, color='blue')
    ax.set_xlabel('Doctors')
    ax.set_ylabel('Number of Patients')
    ax.set_title('Total Number of Patients per Doctor')
    return fig

def plot_bar_chart_appointments():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(doctors, appointments_per_doctor, color='green')
    ax.set_xlabel('Doctors')
    ax.set_ylabel('Number of Appointments')
    ax.set_title('Total Number of Appointments per Month per Doctor')
    return fig

def plot_pie_chart_illness():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(patients_per_illness, labels=illness_types, autopct='%1.1f%%', startangle=140)
    ax.set_title('Total Number of Patients Based on Illness Type')
    ax.axis('equal')
    return fig
