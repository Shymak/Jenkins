# Створюємо порожній список для зберігання клієнтів
clients = []

# 1. Функція для додавання клієнта
def add_client(name, car_model, service_date):
    client = {
        'name': name,
        'car_model': car_model,
        'service_date': service_date
    }
    clients.append(client)
    print(f"Клієнт {name} доданий.")

# 2. Функція для видалення клієнта за іменем
def remove_client(name):
    global clients
    clients = [client for client in clients if client['name'] != name]
    print(f"Клієнт {name} видалений.")

# 3. Функція для отримання списку всіх клієнтів
def get_all_clients():
    if clients:
        for i, client in enumerate(clients, 1):
            print(f"{i}. Ім'я: {client['name']}, Авто: {client['car_model']}, Дата: {client['service_date']}")
    else:
        print("Список клієнтів порожній.")

# 4. Функція для пошуку клієнта за іменем
def find_client(name):
    for client in clients:
        if client['name'] == name:
            return client
    return None

# 5. Функція для оновлення інформації про клієнта
def update_client(name, new_car_model=None, new_service_date=None):
    client = find_client(name)
    if client:
        if new_car_model:
            client['car_model'] = new_car_model
        if new_service_date:
            client['service_date'] = new_service_date
        print(f"Інформація про клієнта {name} оновлена.")
    else:
        print(f"Клієнт {name} не знайдений.")

# Меню для користувача
def menu():
    while True:
        print("\n--- Меню ---")
        print("1. Додати клієнта")
        print("2. Видалити клієнта")
        print("3. Показати всіх клієнтів")
        print("4. Пошук клієнта")
        print("5. Оновити інформацію про клієнта")
        print("6. Вийти")

        choice = input("Виберіть дію (1-6): ")

        if choice == '1':
            name = input("Введіть ім'я клієнта: ")
            car_model = input("Введіть модель авто: ")
            service_date = input("Введіть дату обслуговування (YYYY-MM-DD): ")
            add_client(name, car_model, service_date)

        elif choice == '2':
            name = input("Введіть ім'я клієнта для видалення: ")
            remove_client(name)

        elif choice == '3':
            print("\nСписок всіх клієнтів:")
            get_all_clients()

        elif choice == '4':
            name = input("Введіть ім'я клієнта для пошуку: ")
            client = find_client(name)
            if client:
                print(f"Знайдено клієнта: Ім'я: {client['name']}, Авто: {client['car_model']}, Дата: {client['service_date']}")
            else:
                print(f"Клієнт {name} не знайдений.")

        elif choice == '5':
            name = input("Введіть ім'я клієнта для оновлення: ")
            new_car_model = input("Введіть нову модель авто (або залиште порожнім, щоб не змінювати): ")
            new_service_date = input("Введіть нову дату обслуговування (або залиште порожнім, щоб не змінювати): ")
            update_client(name, new_car_model if new_car_model else None, new_service_date if new_service_date else None)

        elif choice == '6':
            print("Вихід з програми...")
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")

# Запуск меню
menu()
