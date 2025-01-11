from database import db

def show_models():
    for model in db.select_all_models():
        print(f"{model[0]}. Name: {model[1]}")

def a(name: str, count: int):
    return name.center(count, " ") + ' ' + '|'

def show_cars(model_id: int):
    print('-' * 145)
    print('|', a("ID", 8), a("NOMI", 102), a("QUVVATI", 8), a("NARXI", 8), a("MODEL_ID", 8))
    for car in db.select_cars_by_model_id(model_id):
        pass
    print('-' * 145)

def show_colors():
    for color in db.select_colors():
        print(f"{color[0]}. {color[1]}")

def show_list_employees():
    for employee in db.select_employees():
        print(f"{employee[0]}. {employee[1]}")

def show_info_employee(employee_id: int):
    for emplyee in db.show_info_employee(employee_id):
        print(f"{emplyee[0]}. {emplyee[1]}\n"
              f"Maosh: {emplyee[2]}\n"
              f"Lavozimi: {emplyee[3]}")


def run():
    while True:
        command = input("Buyruqni kiriting: ").lower()
        if command == 'stop':
            print("Dastur to'xtadi!!!")
            break
        elif command == 'add model':
            while True:
                model = input("Avtomobil modelini kiriting (exit - chiqish)")
                if model.lower() == 'exit':
                    break

                db.insert_model(model)
                print("Model qo'shildi✅")
        elif command == 'add car':
            while True:
                name = input("Avtomobil nomini kiriting (exit - chiqish): ")

                if name.lower() == 'exit':
                    break

                power = input("Avtomobil ot kuchini kiriting: ")
                price = input("Avtomobil narxini kiriting: ")

                show_models()

                model_id = input("Avtomobil modelini id sini kiriting: ")

                show_colors()

                color_id = input("Rangni tanlang (rangni id raqamini kiriting): ")
                if power.isdigit() and price.isdigit() and model_id.isdigit():
                    db.insert_car(name, int(power), float(price), int(model_id), int(color_id))
                    print("Car qo'shildi✅✅")
        elif command == 'show cars':
            show_models()
            model_id = input('Model id ni kiriting: ')
            if model_id.isdigit():
                show_cars(int(model_id))
        elif command == 'add employee':
            while True:
                name = input("Ishchining ism va familiyasini kiriting (exit - chiqish): ")
                if name == 'exit':
                    break
                oylik = input("Oylik maoshni kiriting: ")
                lavozimi = input("Lavozimni kiriting: ")
                if oylik.isdigit():
                    db.insert_employee(name, int(oylik), lavozimi)
                    print("ishchi qo'shildi✅✅✅")
        elif command == 'list employees':
            show_list_employees()
        elif command == 'show info employee':
            show_list_employees()
            employee_id = input("ishchining id sini kiriting: ")
            if employee_id.isdigit():
                show_info_employee(int(employee_id))
            else:
                print("ishchining id sini faqat raqamda kiriting!!")

if __name__ == '__main__':
    # db.drop_table_models()
    db.create_table_models()

    db.create_table_colors()

    db.create_table_cars()

    db.create_table_employees()

    run()