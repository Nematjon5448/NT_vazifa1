from database_12 import db

def run():
    while True:
        command = input("Buyuruqni kirting (exit - chiqish): ")
        if command == "exit":
            print("Siz Dasturni tark etdingiz ⛔️⛔️⛔️")
            break

        elif command == "add category":
            while True:
                category = input('Kategoriya nomini kiriting (back - ortga): ')
                if category == 'back':
                    break
                db.insert_into_categories(category)
                print("-Kategoriya yaratildi-")

        elif command == 'show categories':
            result = db.select_categories()
            for i in result:
                print(f"{i[0]}. {i[1].title()}")

        elif command == 'add product':
            product_name = input('Mahsulot nomini kiriting (back - ortga): ')
            if product_name == 'back':
                break
            price = input('Mahsulot narxini kiriting (back - ortga): ')
            if price == 'back':
                break
            quantity = input('Mahsulot miqdorini kiriting (back - ortga): ')
            if quantity == 'back':
                break
            untill = input('Mahsulot yaroqlilik muddatini kiriting (dd.mm.yyyy shu formatda kiriting),(back - ortga): ')
            if untill == 'back':
                break
            result = db.select_categories()
            for i in result:
                print(f"{i[0]}. {i[1].title()}")
            category_id = input('Mahsulot kategoriyasini tanlang (kategoriya id raqamini kiriting): ')
            if untill == 'back':
                break
            if price.isdigit() and quantity.isdigit() and category_id.isdigit():
                db.insert_into_product(product_name, int(price), int(quantity), untill, category_id)
                print("Mahsulot qo'shildi")

        elif command == 'show products':
            result = db.select_products()
            for i in result:
                print(f"{i[0]}. {i[1]}")

        elif command == 'add comment':
            while True:
                result = db.select_products()
                for i in result:
                    print(f"{i[0]}. {i[1]}")
                product_id = input("Kommentariya yozmoqchi bo'lgan mahsulotingizni id sini kiriting: ")
                if product_id == 'back':
                    break
                comment = input("Izoh qoldiring: ")
                if comment == 'back':
                    break
                comment_user = input("Ismingizni kirting: ")
                if comment_user == 'back':
                    break
                if product_id.isdigit():
                    db.insert_into_comments(comment, product_id, comment_user)
                    print("Izoh qo'shildi")

        elif command == 'show comments':
            result = db.select_comments()
            for i in result:
                print(f"{i[0]}. Mahsulot_id {i[3]}. {i[1]} ({i[4]})({i[2]})")

if __name__ == '__main__':
    # db.drop_tables()
    db.create_table_categories()
    db.create_table_products()
    db.create_table_comments()
    run()
