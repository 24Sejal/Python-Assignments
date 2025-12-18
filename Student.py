def create_file():
    with open("Student.txt", "w") as file:
        file.write("sejal, 20, cs\n")
        file.write("Chanchal, 21, IT\n")
        file.write("sanika, 22, ECE\n")
    print("Student.txt created and records added")

def read_file():
    with open("Student.txt", "r") as file:
        print("\nStudent Records:")
        print(file.read())

def append_record():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open("Student.txt", "a") as file:
        file.write(f"{name}, {age}, {course}\n")
    print("Record added sucessfully")

def count_records():
    with open("Student.txt", "r") as file:
        lines = file.readlines()
        print("Total students records:", len(lines))

def search_student():
    search_name = input("Enter student name to search:")
    found = False

    with open("Student.txt", "r") as file:
        for line in file:
            if search_name.lower() in line.lower():
                print("Student found:", line)
                found = True
                break
    if not found:
        print("Student not found")

while True:
    print("\n --- Student Record file handling ---")
    print("1. Create file and write records")
    print("2. Read all records")
    print("3. Append new record")
    print("4. Count total records")
    print("5. Search students")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        create_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        append_record()
    elif choice == "4":
        count_records()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Program Exited")
        break
    else:
        print("Invalid choice")

