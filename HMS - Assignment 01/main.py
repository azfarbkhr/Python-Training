# need to build a hospital management system

# import the libraries 
import pandas as pd
import datetime
import numpy as np
import os 


# some helper functions
clear = lambda: os.system('clear')


def print_heading(heading):
    clear()
    print("#" * 20)
    print(heading)
    print("#" * 20)

def save_patients(patient_list, message):
    while True:
        try:
            patient_list.to_csv("patients.csv", index=False)
            print_heading(message)
            input("Press enter to continue to main menu.")
            break
        except PermissionError:
            print_heading("ERROR: Please close the patients.csv file and try again.")
            input("Press enter to try again.")


# business logic related functions
def print_menu():
    print_heading("HMS - Main Menu")
    print("1. Patient Menu")
    print("11. Rooms Menu")
    print("21. Exit")

    user_input = input("Please enter option code: ")

    if user_input == "21":
        return user_input

    elif user_input == "1":
        print_heading("Patient Menu")
        print("1. Add Patient")
        print("2. Update Patient")
        print("3. Find Patient by ID")
        print("4. View Active Patients")
        print("5. Add bill amount")
        print("21. Exit")
        user_input = input("Please enter option code: ")

    elif user_input == "11":
        print_heading("Rooms Menu")
        print("11. Add Room")
        print("12. Update Room")
        print("13. Assign Room to Patient")
        print("14. View Available Rooms")
        print("21. Exit")
        user_input = input("Please enter option code: ")
    else:
        user_input = "0"

    return user_input

# add patient function
def add_patient():
    print_heading("To add a new patient, please provide the following details;")
    
    # get patient details    
    patient_name = input("Enter patient name: ")
    patient_admission_status = "Admitted"
    patient_dob = input("Enter patient date of birth: ")
    patient_admission_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    patient_diagnosis = input("Enter patient diagnosis: ")

    # access the patient list 
    patient_list = pd.read_csv("patients.csv")

    # get the last patient id
    last_patient_id = patient_list["Patient ID"].max()

    # create a new patient id
    new_patient_id = last_patient_id + 1

    # create a new patient row
    new_patient_row = pd.DataFrame([[new_patient_id, patient_name, patient_admission_status, patient_dob, patient_admission_date, patient_diagnosis]], columns=["Patient ID", "Patient Name", "Admission Status", "Date of Birth", "Admission Date", "Diagnosis"])

    # append the new patient row to the patient list
    patient_list = pd.concat([patient_list, new_patient_row], ignore_index=True)
    
    # save the patient list
    save_patients(patient_list=patient_list, message="SUCCESS: Patient added successfully! (Patient ID = " + str(new_patient_id) + ")")


# update patient function
def update_patient():
    print_heading("To update an existing patient, please provide the following details, leave the field to not update the data;")

    while True:
        try: 
            patient_id = int(input("Enter patient ID: "))
            break
        except ValueError:
            print_heading("ERROR: Please enter a valid patient ID.")
            input("Press enter to try again.")


    # access the patient list
    patient_list = pd.read_csv("patients.csv")

    # check if patient id exists
    if patient_id in patient_list["Patient ID"].values:

        patient_row = patient_list.loc[patient_list["Patient ID"] == int(patient_id)]

        # print the patient row
        print_heading("Patient Current Details")
        print("Patient ID: ", patient_row["Patient ID"].values[0])
        print("Patient Name: ", patient_row["Patient Name"].values[0])
        print("Admission Status: ", patient_row["Admission Status"].values[0])
        print("Date of Birth: ", patient_row["Date of Birth"].values[0])
        print("Admission Date: ", patient_row["Admission Date"].values[0])
        print("Diagnosis: ", patient_row["Diagnosis"].values[0])
        print("#" * 20)
        input("Press enter to continue to main menu.")
        print("#" * 20)

        # get patient details    
        patient_name = input("Enter patient name: ")
        patient_admission_status = input("Enter patient admission status: ")
        patient_dob = input("Enter patient date of birth: ")
        patient_admission_date = input("Enter patient admission date: ")
        patient_diagnosis = input("Enter patient diagnosis: ")

        # update the patient row
        if patient_name != "":
            patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Patient Name"] = patient_name
        
        if patient_admission_status != "":
            patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Admission Status"] = patient_admission_status
        
        if patient_dob != "":
            patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Date of Birth"] = patient_dob
        
        if patient_admission_date != "":
            patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Admission Date"] = patient_admission_date
        
        if patient_diagnosis != "":
            patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Diagnosis"] = patient_diagnosis


        # save the patient list
        save_patients(patient_list=patient_list, message="SUCCESS: Patient updated successfully! (Patient ID = " + str(patient_id) + ")")

    else:
        print_heading("ERROR: Patient ID does not exist. " + "\nAvailable patient IDs are: " + str(patient_list["Patient ID"].values))
        input("Press enter to try again.")

# find patient by id function
def find_patient_by_id():
    print_heading("To find a patient, please provide the following details;")

    while True:
        try: 
            patient_id = int(input("Enter patient ID: "))
            break
        except ValueError:
            print_heading("ERROR: Please enter a valid patient ID.")
            input("Press enter to try again.")

    # access the patient list
    patient_list = pd.read_csv("patients.csv")

    # check if patient id exists
    if patient_id in patient_list["Patient ID"].values:
        # get the patient row
        patient_row = patient_list.loc[patient_list["Patient ID"] == int(patient_id)]

        # print the patient row
        print("#" * 20)
        print("Patient ID: ", patient_row["Patient ID"].values[0])
        print("Patient Name: ", patient_row["Patient Name"].values[0])
        print("Admission Status: ", patient_row["Admission Status"].values[0])
        print("Date of Birth: ", patient_row["Date of Birth"].values[0])
        print("Admission Date: ", patient_row["Admission Date"].values[0])
        print("Diagnosis: ", patient_row["Diagnosis"].values[0])
        print("#" * 20)
        input("Press enter to continue to main menu.")
        print("#" * 20)
    else:
        print_heading("ERROR: Patient ID does not exist. " + "\nAvailable patient IDs are: " + str(patient_list["Patient ID"].values))
        input("Press enter to continue to main menu.")

# View Active Patients
def view_active_patients():
    # access the patient list
    patient_list = pd.read_csv("patients.csv")

    # get active patients
    active_patients = patient_list.loc[patient_list["Admission Status"] != "Discharged"]

    # print active patients
    print_heading("Active Patients")
    print(active_patients)
    print("#" * 20)
    input("Press enter to continue to main menu.")

# add bill function
def add_bill():
    # access the patient list
    patient_list = pd.read_csv("patients.csv")

    # get the patient id
    while True:
        try: 
            patient_id = int(input("Enter patient ID: "))
            break
        except ValueError:
            print_heading("ERROR: Please enter a valid patient ID.")

    # check if patient id exists
    if patient_id in patient_list["Patient ID"].values:
        # get the patient row
        
        pending_amount = patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Pending Amount"].values[0] 

        # if nan then set to 0 using numpy
        if np.isnan(pending_amount):
            pending_amount = 0

        # get the bill details
        print("Payment received should be entered as positive and amount charged as negative.")
        transaction_amount = input("Enter transaction amount: ")

        # update the patient row pending bill amount 
        patient_list.loc[patient_list["Patient ID"] == int(patient_id), "Pending Amount"] = float(pending_amount) + float(transaction_amount)

        # save the patient list
        save_patients(patient_list, "SUCCESS: Bill added successfully! (Patient ID = " + str(patient_id) + ")")

    else:
        print_heading("ERROR: Patient ID does not exist. " + "\nAvailable patient IDs are: " + str(patient_list["Patient ID"].values))
        input("Press enter to continue to main menu.")


# the main application 
while True:
    user_input = print_menu()

    if user_input == "21":
        print("Exiting...")
        break
    
    elif user_input == "1":
        add_patient()

    elif user_input == "2":
        update_patient()

    elif user_input == "3":
        find_patient_by_id()

    elif user_input == "4":
        view_active_patients()

    elif user_input == "5":
        add_bill()

    else:
        print_heading("ERROR: Please enter a valid option code.")
        input("Press enter to try again.")
        continue
    