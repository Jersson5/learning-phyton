import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Creación de la tabla students
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    code VARCHAR(50) NOT NULL,
                    id_person INTEGER NOT NULL,
                    status BOOLEAN NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL,
                    FOREIGN KEY (id_person) REFERENCES persons(id)
                )''')

# Creación de la tabla users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    email VARCHAR(100) NOT NULL,
                    password VARCHAR(250) NOT NULL,
                    status BOOLEAN NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL,
                    UNIQUE(email)
                )''')

# Creación de la tabla identification_types
cursor.execute('''CREATE TABLE IF NOT EXISTS identification_types (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(100) NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL
                )''')

# Creación de la tabla persons
cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
                    id INTEGER PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    ident_number VARCHAR(15) NOT NULL,        
                    adress VARCHAR(150) NOT NULL,
                    mobile VARCHAR(100) NOT NULL,
                    id_user INTEGER NOT NULL,
                    id_ident_type INTEGER NOT NULL,
                    id_exp_city INTEGER NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL,
                    FOREIGN KEY (id_ident_type) REFERENCES identification_types(id),
                    FOREIGN KEY (id_exp_city) REFERENCES cities(id)
                )''')

# Creación de la tabla cities
cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(10) NOT NULL,
                    id_dept INTEGER NOT NULL,      
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL,
                    FOREIGN KEY (id_dept) REFERENCES departments(id)  
                )''')

# Creación de la tabla departments
cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(10) NOT NULL, 
                    id_country INTEGER NOT NULL, 
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL,
                    FOREIGN KEY (id_country) REFERENCES countries(id)  
                )''')

# Creación de la tabla countriea
cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(10) NOT NULL,        
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleted_at DATETIME NULL 
                )''')
# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()