def store_student_details(filename):
    with open(filename, 'a') as file:
        while True:
            roll_number = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = input("Enter marks: ")
            file.write(f"{roll_number},{name},{marks}\n")
            cont = input("Enter y if you want to add another student: ")
            if cont.lower() != 'y':
                break

store_student_details("Marks.data")
