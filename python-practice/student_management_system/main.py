student_details = []

def add_student():
    student_id = input("Enter Student ID :")
    student_name = input("Enter Student Name : ")
    student_gpa = float(input("Enter GPA of the student : "))
    student_record = {'id': student_id, 'Name': student_name, 'GPA': student_gpa}
    student_details.append(student_record)
    print("Student added successfully.")

def remove_student():
    removing_student_record = input("Enter Student ID : ")
    student_found = False
    for i in student_details:
        if i['id'] == removing_student_record:
            student_details.remove(i)
            print("Student Record Deleted Successfully.")
            student_found = True
            break
    
    if not student_found:
        print("Student Record Not Found !")

def search_student():
    search_term = input('Enter Id or Name :')
    student_found = False

    if len(student_details) > 0:
        for i in student_details:
            if i['id'] == search_term or i['Name'] == search_term :
                print('Student ID : ', i['id'])
                print('Student Name : ', i['Name'])
                print('Student GPA :', i['GPA'])
                student_found = True
                break
        if not student_found:
            print("No Student Record found !")
        
    else: 
        print("No Student Records Found !")

def display_student():
    if len(student_details) == 0:
        print("No Student Records Found.")
    else:
        for i in student_details:
            print("---------------------------------------")
            print('Student ID :', i['id'])
            print('Student Name :', i['Name'])
            print('Student GPA :', i['GPA'])
            # print('\n')
        




while True:
    print("===Student Management System ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    print(' ')
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        display_student()
    elif choice == 5:
        break
    else:
        print("Please enter Valid option.")



