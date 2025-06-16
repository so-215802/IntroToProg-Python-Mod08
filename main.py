# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Starter files
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# Seth Overbay, 06/16/2025, Created Script
# ------------------------------------------------------------------------------------------------- #

import json
import data_classes as data
import processing_classes as proc
import presentation_classes as pres
from datetime import date

# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                       employee_data=data.employees,
                                                       employee_type=data.Employee)  # Note this is the class name (ignore the warning)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees, employee_type=data.Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=data.employees)
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop