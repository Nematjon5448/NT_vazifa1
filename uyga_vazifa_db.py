import psycopg2

try:
    db = psycopg2.connect(
        dbname='Uyga_vazifa_3dars',
        user='postgres',
        password='5448',
        host='localhost',
    )

    cursor = db.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS attendance;
    DROP TABLE IF EXISTS grade;
    DROP TABLE IF EXISTS enrollment;
    DROP TABLE IF EXISTS subject;
    DROP TABLE IF EXISTS sinf;
    DROP TABLE IF EXISTS student;
    DROP TABLE IF EXISTS teacher;
    DROP TABLE IF EXISTS maktab;
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS school(
        school_id SERIAL PRIMARY KEY,
        school_name VARCHAR(100),
        address VARCHAR(100),
        phone_number CHAR(13),
        davlat_maktabi BOOL
    );
    CREATE TABLE IF NOT EXISTS teacher(
        teacher_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        email VARCHAR(100),
        phone_number CHAR(13),
        school_id INTEGER REFERENCES school(school_id)
    );
    CREATE TABLE IF NOT EXISTS student(
        student_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        date_of_birth DATE,
        gender VARCHAR(10),
        school_id INTEGER REFERENCES school(school_id)
    );
    CREATE TABLE IF NOT EXISTS class(
        class_id SERIAL PRIMARY KEY,
        class_name VARCHAR(50),
        teacher_id INTEGER REFERENCES teacher(teacher_id),
        school_id INTEGER REFERENCES school(school_id)
    );
    CREATE TABLE IF NOT EXISTS subject(
        subject_id SERIAL PRIMARY KEY,
        subject_name VARCHAR(50),
        class_id INTEGER REFERENCES class(class_id),
        teacher_id INTEGER REFERENCES teacher(teacher_id)
    );
    CREATE TABLE IF NOT EXISTS enrollment(
        enrollment_id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES student(student_id),
        class_id INTEGER REFERENCES class(class_id),
        enrollment_date DATE DEFAULT CURRENT_DATE
    );
    CREATE TABLE IF NOT EXISTS grade(
        grade_id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES student(student_id),
        subject_id INTEGER REFERENCES subject(subject_id),
        grade_value INTEGER,
        date_given DATE DEFAULT CURRENT_DATE
    );
    CREATE TABLE IF NOT EXISTS attendance(
        attendance_id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES student(student_id),
        class_id INTEGER REFERENCES class(class_id),
        date DATE DEFAULT CURRENT_DATE
    );
    ''')

    cursor.execute('''
        INSERT INTO school(school_name, address, phone_number, davlat_maktabi)
        VALUES  ('TERRA NOVA', 'Farg''ona sh. Bahor ko''chasi 138', '+998976657565', FALSE),
            ('SIRIUS', 'Farg''ona sh. Farg''ona ko''chasi 130A', '+998732412002', FALSE),
            ('11 - Umumiy o''rta ta''lim maktabi', 'Marg''ilon sh. Mustaqillik ko''chasi ', '+998901234567', TRUE),
            ('RAHIMOV SCHOOL', 'Farg''ona sh. Mustaqillik ko''chasi 39/136', '+998781130005', FALSE);

        INSERT INTO teacher(first_name, last_name, email, phone_number, school_id)
        VALUES  ('Shavkat', 'Hakimov', 'hakimovsh@gmail.com', '+998936444033', 2),
            ('Shoxrux', 'Abdusamatov', 'abdusamatovsh@mail.ru', '+998911222422', 1),
            ('Saidazimxon', 'Mamurxonov', 'saidazimxonm@gmail.com', '+998939786565', 3),
            ('Ziyodullo', 'Mirzaliyev', 'mirzaliyevziyodullo@gmail.com', '+998905857882', 4);

        INSERT INTO student(first_name, last_name, date_of_birth, gender, school_id)
        VALUES  ('Nematjon', 'Rasulov', TO_DATE('01.05.2002', 'dd.mm.yyyy'), 'boy', 3),
            ('Avazxon', 'Abdurasulov', TO_DATE('03.08.2001', 'dd.mm.yyyy'), 'boy', 1),
            ('Abdullo', 'Sobirjonov', TO_DATE('18.06.2003', 'dd.mm.yyyy'), 'boy', 2),
            ('Ikrom', 'Akramov', TO_DATE('20.01.2000', 'dd.mm.yyyy'), 'boy', 4);

        INSERT INTO class(class_name, teacher_id, school_id)
        VALUES  ('9-A', 3, 3),
            ('8-B', 1, 2),
            ('10-D', 2, 1),
            ('11-A', 4, 4);

        INSERT INTO subject(subject_name, class_id, teacher_id)
        VALUES  ('Matematika', 1, 3),
            ('Fizika', 2, 1),
            ('Adabiyot', 3, 2),
            ('Jismoniy tarbiya', 4, 4);

        INSERT INTO enrollment(student_id, class_id)
        VALUES  (1, 1),
            (2, 3),
            (3, 2),
            (4, 4);

        INSERT INTO grade(student_id, subject_id, grade_value)
        VALUES  (1, 1, 5),
            (2, 3, 4),
            (3, 2, 4),
            (4, 4, 5);

        INSERT INTO attendance(student_id, class_id)
        VALUES  (1, 1),
            (2, 3),
            (3, 2),
            (4, 4);
    ''')

    cursor.execute('''SELECT * FROM school;''')
    maktab = cursor.fetchall()
    print(maktab)

    cursor.execute('''SELECT * FROM student;''')
    oquvchi = cursor.fetchall()
    print(oquvchi)

    cursor.execute('''
    ALTER TABLE IF EXISTS school
    RENAME TO maktab;

    ALTER TABLE IF EXISTS class
    RENAME TO sinf;

    ALTER TABLE IF EXISTS maktab
    RENAME COLUMN school_name TO maktab_nomi;
    
    ALTER TABLE IF EXISTS maktab
    RENAME COLUMN address TO manzil;

    ALTER TABLE IF EXISTS teacher
    RENAME COLUMN phone_number TO telefon_raqam;

    ALTER TABLE IF EXISTS maktab
    ADD COLUMN web_sahifa VARCHAR(100);

    ALTER TABLE IF EXISTS teacher
    ADD COLUMN malumoti VARCHAR(100);

    ALTER TABLE IF EXISTS maktab
    DROP COLUMN web_sahifa;

    UPDATE subject SET subject_name = 'Ingliz tili' WHERE subject_id = 1;
    UPDATE subject SET subject_name = 'Adabiyot' WHERE subject_id = 3;
    UPDATE sinf SET class_name = '9-A' WHERE class_id = 1;
    UPDATE sinf SET class_name = '9-D' WHERE class_id = 4;

    DELETE FROM grade WHERE grade_id = 1;
    DELETE FROM attendance WHERE attendance_id = 2;
    ''')

    db.commit()
    db.close()
except:
    print("---------------------ERROR-------------------------")