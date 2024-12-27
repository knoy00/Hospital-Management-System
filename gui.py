import tkinter as tk
from tkinter import messagebox
from diagrams import plot_total_doctors, plot_bar_chart_patients, plot_bar_chart_appointments, plot_pie_chart_illness
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def display_chart(fig):
    canvas = FigureCanvasTkAgg(fig, master=report_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def display_total_doctors():
    fig = plot_total_doctors()
    display_chart(fig)

def display_bar_chart_patients():
    fig = plot_bar_chart_patients()
    display_chart(fig)

def display_bar_chart_appointments():
    fig = plot_bar_chart_appointments()
    display_chart(fig)

def display_pie_chart_illness():
    fig = plot_pie_chart_illness()
    display_chart(fig)

def view_reports():
    global report_frame  # Declare the variable as global

    report_window = tk.Toplevel(root)
    report_window.title("Reports")
    report_window.geometry("800x600")

    # Create a frame and canvas with scrollbar
    report_canvas = tk.Canvas(report_window)
    scrollbar = tk.Scrollbar(report_window, orient="vertical", command=report_canvas.yview)
    report_frame = tk.Frame(report_canvas)

    report_frame.bind(
        "<Configure>",
        lambda e: report_canvas.configure(
            scrollregion=report_canvas.bbox("all")
        )
    )

    report_canvas.create_window((0, 0), window=report_frame, anchor="nw")
    report_canvas.configure(yscrollcommand=scrollbar.set)

    report_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Add buttons for the reports inside the scrollable frame
    btn_total_doctors = tk.Button(report_frame, text="Total Number of Doctors", command=display_total_doctors)
    btn_total_doctors.pack(pady=10)

    btn_patients_per_doctor = tk.Button(report_frame, text="Total Patients per Doctor", command=display_bar_chart_patients)
    btn_patients_per_doctor.pack(pady=10)

    btn_appointments_per_doctor = tk.Button(report_frame, text="Appointments per Month per Doctor", command=display_bar_chart_appointments)
    btn_appointments_per_doctor.pack(pady=10)

    btn_illness_type = tk.Button(report_frame, text="Patients Based on Illness Type", command=display_pie_chart_illness)
    btn_illness_type.pack(pady=10)

    # Display text to make user scroll to the bottom to view all reports
    tk.Label(report_frame, text="Scroll down to view all reports if all opened").pack()

def main():
    global root, report_frame
    root = tk.Tk()
    root.title("Hospital Management System")
    root.geometry("600x400")

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    function_menu = tk.Menu(menu)
    menu.add_cascade(label="Functions", menu=function_menu)
    function_menu.add_command(label="View Reports", command=view_reports)

    root.mainloop()

if __name__ == "__main__":
    main()
