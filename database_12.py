import psycopg2

class Database:
    def __init__(self, dbname:str, user:str, password:str, host:str, port: int=5432):
        self.database = psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            host = host,
            port = port
            )

    def manager(self, sql, *args, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                result = None
                if fetchall:
                    result = cursor.fetchall()
            return result

    def drop_tables(self):
        sql = '''
                DROP TABLE IF EXISTS comments CASCADE;
                DROP TABLE IF EXISTS products CASCADE;
                DROP TABLE IF EXISTS categories CASCADE;
              '''
        self.manager(sql)

    def create_table_categories(self):
        sql = '''
                CREATE TABLE IF NOT EXISTS categories(
                categories_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                categories_name VARCHAR(50) UNIQUE
                )
              '''
        self.manager(sql)

    def insert_into_categories(self, category: str):
        sql = """
                INSERT INTO categories(categories_name) 
                VALUES (%s) ON CONFLICT DO NOTHING 
              """
        self.manager(sql, category)

    def select_categories(self):
        sql = """
                SELECT * FROM categories;
              """
        return self.manager(sql, fetchall=True)

    def create_table_products(self):
        sql = """
                CREATE TABLE IF NOT EXISTS products(
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(100),
                price INTEGER,
                quantity INTEGER,
                untill DATE,
                categories_id INTEGER REFERENCES categories(categories_id)
                )
              """
        self.manager(sql)

    def insert_into_product(self, product_name: str, price: int, quantity: int, untill: str, categories_id: int):
        sql = '''
                INSERT INTO products(product_name, price, quantity, untill, categories_id)
                VALUES  (%s, %s, %s, TO_DATE(%s, 'dd.mm.yyyy'), %s)
              '''
        self.manager(sql, product_name, price, quantity, untill, categories_id)

    def select_products(self):
        sql = '''
                SELECT product_id, product_name FROM products;
              '''
        return self.manager(sql, fetchall=True)

    def create_table_comments(self):
        sql = """
                CREATE TABLE IF NOT EXISTS comments(
                comment_id SERIAL PRIMARY KEY,
                text TEXT,
                created DATE DEFAULT CURRENT_DATE,
                product_id INTEGER REFERENCES products(product_id),
                comment_user VARCHAR(40)
                )
              """
        self.manager(sql)

    def insert_into_comments(self, text: str, product_id: int, comment_user: str):
        sql = '''
                INSERT INTO comments(text, product_id, comment_user)
                VALUES  (%s, %s, %s)
              '''
        self.manager(sql, text, product_id, comment_user)

    def select_comments(self):
        sql = '''
                SELECT * FROM comments;
              '''
        return self.manager(sql, fetchall=True)

db = Database('shop', 'postgres', '5448', 'localhost')

