import sqlite3

def create_country(conn):
    print("Creating a new country...")
    name = input("Enter country name: ")
    abrev = input("Enter country abbreviation: ")
    descrip = input("Enter country description: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO countries (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, datetime('now'), datetime('now'))", (name, abrev, descrip))
    conn.commit()
    print("Country created successfully.")

def create_department(conn):
    print("Creating a new department...")
    name = input("Enter department name: ")
    abrev = input("Enter department abbreviation: ")
    descrip = input("Enter department description: ")
    id_country = int(input("Enter country ID: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO departments (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))", (name, abrev, descrip, id_country))
    conn.commit()
    print("Department created successfully.")

def create_city(conn):
    print("Creating a new city...")
    name = input("Enter city name: ")
    abrev = input("Enter city abbreviation: ")
    descrip = input("Enter city description: ")
    id_dept = int(input("Enter department ID: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at) VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))", (name, abrev, descrip, id_dept))
    conn.commit()
    print("City created successfully.")

def create_identification_type(conn):
    print("Creating a new identification type...")
    name = input("Enter identification type name: ")
    abrev = input("Enter identification type abbreviation: ")
    descrip = input("Enter identification type description: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, datetime('now'), datetime('now'))", (name, abrev, descrip))
    conn.commit()
    print("Identification type created successfully.")

def create_user(conn):
    print("Creating a new user...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    status = input("Enter status (True/False): ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password, status, created_at, updated_at) VALUES (?, ?, ?, datetime('now'), datetime('now'))", (email, password, status))
    conn.commit()
    print("User created successfully.")

def create_person(conn):
    print("Creating a new person...")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    ident_number = input("Enter identification number: ")
    address = input("Enter address: ")
    mobile = input("Enter mobile number: ")
    id_user = int(input("Enter user ID: "))
    id_ident_type = int(input("Enter identification type ID: "))
    id_exp_city = int(input("Enter city ID for experience: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO persons (first_name, last_name, ident_number, adress, mobile, id_user, id_ident_type, id_exp_city, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))", (first_name, last_name, ident_number, address, mobile, id_user, id_ident_type, id_exp_city))
    conn.commit()
    print("Person created successfully.")

def create_student(conn):
    print("Creating a new student...")
    code = input("Enter code: ")
    id_person = int(input("Enter person ID: "))
    status = input("Enter status (True/False): ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (code, id_person, status, created_at, updated_at) VALUES (?, ?, ?, datetime('now'), datetime('now'))", (code, id_person, status))
    conn.commit()
    print("Student created successfully.")

def main():
    conn = sqlite3.connect('school.db')

    while True:
        print("\nMain menu")
        print("[1]. Create country")
        print("[2]. Create department")
        print("[3]. Create city")
        print("[4]. Create identification type")
        print("[5]. Create user")
        print("[6]. Create person")
        print("[7]. Create student")
        print("[8]. EXIT")

        choice = input("Select an option: ")

        if choice == '1':
            create_country(conn)
        elif choice == '2':
            create_department(conn)
        elif choice == '3':
            create_city(conn)
        elif choice == '4':
            create_identification_type(conn)
        elif choice == '5':
            create_user(conn)
        elif choice == '6':
            create_person(conn)
        elif choice == '7':
            create_student(conn)
        elif choice == '8':
            break
        else:
            print("Invalid option. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
