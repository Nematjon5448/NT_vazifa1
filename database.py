import psycopg2

class Database:
    def __init__(self, dbname: str, user: str, password: str, host: str, port: int = 5432):
        self.database = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def manager(self, sql, *args, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                result = None
                if fetchall:
                    result = cursor.fetchall()
            return result

    def drop_table_models(self):
        sql = '''DROP TABLE IF EXISTS employees;
        DROP TABLE IF EXISTS colors CASCADE;
        DROP TABLE IF EXISTS cars;
        DROP TABLE IF EXISTS models;
        '''
        self.manager(sql)

    def create_table_models(self):
        sql = '''CREATE TABLE IF NOT EXISTS models(
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(100) UNIQUE
        )'''
        self.manager(sql)

    def insert_model(self, model_name):
        sql = '''INSERT INTO models(name) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, model_name)

    def select_all_models(self):
        sql = '''SELECT * FROM models'''
        return self.manager(sql, fetchall=True)

    def create_table_cars(self):
        sql = '''CREATE TABLE IF NOT EXISTS cars(
            cars_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            power INT,
            price NUMERIC(10, 2),
            model_id INTEGER REFERENCES models(id),
            color_id INTEGER REFERENCES colors(color_id)
        )'''
        self.manager(sql)

    def insert_car(self, name: str, power: int, price, model_id: int, color_id: int):
        sql = '''INSERT INTO cars(name, power, price, model_id, color_id) VALUES (%s, %s, %s, %s, %s)'''
        self.manager(sql, name, power, price, model_id, color_id)

    def select_cars_by_model_id(self, model_id):
        sql = '''SELECT * FROM cars WHERE model_id = %s'''
        return self.manager(sql, model_id, fetchall=True)

    def create_table_colors(self):
        sql = '''CREATE TABLE IF NOT EXISTS colors(
            color_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            color_name VARCHAR(20) UNIQUE
            )'''
        def insert_colors():
            sql1 = '''INSERT INTO colors(color_name) VALUES ('sariq'), ('qora'), ('qizil'), ('oq'), ('ko''k'), ('kulrang') ON CONFLICT DO NOTHING'''
            self.manager(sql1)
        self.manager(sql)
        insert_colors()

    def select_colors(self):
        sql = '''SELECT * FROM colors'''
        return self.manager(sql, fetchall=True)

    def create_table_employees(self):
        sql = '''CREATE TABLE IF NOT EXISTS employees(
        employee_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        full_name VARCHAR(50),
        salary INTEGER,
        position VARCHAR(100)
        )'''
        self.manager(sql)

    def insert_employee(self, full_name: str, salary: int, position: str):
        sql = '''INSERT INTO employees(full_name, salary, position)
        VALUES  (%s, %s, %s)'''
        self.manager(sql, full_name, salary, position)

    def select_employees(self):
        sql = '''SELECT * FROM employees'''
        return self.manager(sql, fetchall=True)

    def show_info_employee(self, employee_id: int):
        sql = '''SELECT * FROM employees WHERE employee_id = %s'''
        return self.manager(sql, employee_id, fetchall=True)

db = Database('autosalon', 'postgres', '5448', 'localhost')