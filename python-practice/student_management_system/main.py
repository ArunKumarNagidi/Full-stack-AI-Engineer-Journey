import json

# This is our live runtime list that holds the records in memory
student_details = []

# =====================================================================
# 1. FILE HANDLING & JSON CORE (Data Persistence)
# =====================================================================

def load_data():
    """Loads student records from students.json when the application starts."""
    global student_details
    try:
        with open("students.json", "r") as file:
            student_details = json.load(file)
            print("========================================")
            print("DATABASE LOADED: Existing records synced.")
            print("========================================")
    except FileNotFoundError:
        # First-time run setup: the file doesn't exist yet, which is completely fine
        student_details = []
        print("========================================")
        print("INITIALIZATION: New database initialized.")
        print("========================================")

def save_data():
    """Overwrites students.json with the current student_details list state."""
    with open("students.json", "w") as file:
        json.dump(student_details, file, indent=4)


# =====================================================================
# 2. VALIDATION HELPERS (Input Gatekeepers)
# =====================================================================

def get_valid_name():
    """Ensures names are not empty strings or spaces."""
    while True:
        name = input("Enter Student Name: ").strip()
        if not name:
            print("❌ Error: Student name cannot be empty. Please try again.")
        else:
            return name

def get_valid_gpa():
    """Ensures GPA is a valid float value and within bounds."""
    while True:
        try:
            gpa = float(input("Enter GPA of the student (0.0 - 10.0): "))
            if 0.0 <= gpa <= 10.0:
                return gpa
            else:
                print("❌ Error: GPA boundary out of range. Must be 0.0 - 10.0.")
        except ValueError:
            print("❌ Error: Invalid input format. Please enter a numerical decimal value.")


# =====================================================================
# 3. CORE MANAGEMENT FEATURES (CRUD Business Logic)
# =====================================================================

def add_student():
    student_id = input("Enter Student ID: ").strip()
    
    # Run data through validation checks
    student_name = get_valid_name()
    student_gpa = get_valid_gpa()
    
    student_record = {'id': student_id, 'Name': student_name, 'GPA': student_gpa}
    student_details.append(student_record)
    
    # Trigger auto-save immediately to hard drive
    save_data()
    
    print("\n========================================")
    print("✨ SUCCESS: Student added and backed up!")
    print("========================================")

def remove_student():
    removing_student_record = input("Enter Student ID to remove: ").strip()
    student_found = False
    
    for i in student_details:
        if i['id'] == removing_student_record:
            student_details.remove(i)
            student_found = True
            
            # Trigger auto-save immediately to hard drive
            save_data()
            
            print("\n========================================")
            print("🗑️ SUCCESS: Record deleted and database updated.")
            print("========================================")
            break
    
    if not student_found:
        print("\n❌ Error: Student Record Not Found!")

def search_student():
    search_term = input('Enter ID or Name to search: ').strip()
    student_found = False

    if len(student_details) > 0:
        for i in student_details:
            if i['id'] == search_term or i['Name'].lower() == search_term.lower():
                print("\n========================================")
                print("         📄 STUDENT PROFILE FOUND       ")
                print("========================================")
                print(f"Student ID   : {i['id']}")
                print(f"Student Name : {i['Name']}")
                print(f"Student GPA  : {i['GPA']}")
                print("========================================")
                student_found = True
                break
        if not student_found:
            print("\n🔍 Result: No Student Record matches your search.")
    else: 
        print("\n🗄️ System: The database is currently empty.")

def display_student():
    if len(student_details) == 0:
        print("\n🗄️ System: No Student Records Found.")
    else:
        print("\n========================================")
        print("       📝 LISTING ALL SYSTEM RECORDS    ")
        print("========================================")
        for i in student_details:
            print(f"ID: {i['id']} | Name: {i['Name']} | GPA: {i['GPA']}")
        print("========================================")


# =====================================================================
# 4. APPLICATION RUNTIME BOOTSTRAP
# =====================================================================

# Step A: Load files before launching menu
load_data()

# Step B: Enter execution loop
while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")
    print(' ')
    
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("❌ Error: Invalid menu option format. Please input an option number.")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        display_student()
    elif choice == 5:
        print("\nShutting down core engine safely. Goodbye!")
        break
    else:
        print("❌ Error: Please enter a choice matching the menu metrics (1-5).")




# import json
# import os


# student_details = []

# def add_student():
#     student_id = input("Enter Student ID :")
#     while True:

#         student_name = input("Enter Student Name : ").strip()
#         if not student_name:
#             print("Enter valid Name.")
#         else:
#             break
    

#     while True:
#         try:
#             student_gpa = float(input("Enter GPA of the student (0.0 - 10.0): "))
#             if 0.0 <= student_gpa <= 10.0:
#                 break
#             else:
#                 print("Error: GPA must be between 0.0 and 10.0.")
#         except ValueError:
#             print("Error: Invalid input. Please enter a numerical decimal value for GPA.")
#     # student_gpa = float(input("Enter GPA of the student : "))
#     student_record = {'id': student_id, 'Name': student_name, 'GPA': student_gpa}
#     student_details.append(student_record)
#     save_data()
#     print("Student added successfully.")

# def remove_student():
#     removing_student_record = input("Enter Student ID : ")
#     student_found = False
#     for i in student_details:
#         if i['id'] == removing_student_record:
#             student_details.remove(i)
#             save_data()
#             print("Student Record Deleted Successfully.")
#             student_found = True
#             break
    
#     if not student_found:
#         print("Student Record Not Found !")

# def search_student():
#     search_term = input('Enter Id or Name :')
#     student_found = False

#     if len(student_details) > 0:
#         for i in student_details:
#             if i['id'] == search_term or i['Name'] == search_term :
#                 print('Student ID : ', i['id'])
#                 print('Student Name : ', i['Name'])
#                 print('Student GPA :', i['GPA'])
#                 student_found = True
#                 break
#         if not student_found:
#             print("No Student Record found !")
        
#     else: 
#         print("No Student Records Found !")

# def display_student():
#     if len(student_details) == 0:
#         print("No Student Records Found.")
#     else:
#         for i in student_details:
#             print("---------------------------------------")
#             print('Student ID :', i['id'])
#             print('Student Name :', i['Name'])
#             print('Student GPA :', i['GPA'])
#             # print('\n')

# def save_data():
#     with open('students.json','w') as file :
#         json.dump(student_details, file, indent=4)    

# try:

#     with open('students.json','r') as file:
#         student_details = json.load(file)
# except:
#     student_details = []

# while True:
#     print("===Student Management System ===")
#     print("1. Add Student")
#     print("2. Remove Student")  
#     print("3. Search Student")
#     print("4. Display All Students")
#     print("5. Exit")

#     print(' ')
#     try:
#         choice = int(input("Enter your choice: "))
#     except ValueError:
#         print("Enter valid Input.")
#         continue

#     if choice == 1:
#         add_student()
#     elif choice == 2:
#         remove_student()
#     elif choice == 3:
#         search_student()
#     elif choice == 4:
#         display_student()
#     elif choice == 5:
#         break
#     else:
#         print("Please enter Valid option.")



