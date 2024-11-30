import unittest
from Sto import add_client, remove_client, get_all_clients, find_client, update_client
class TestSTOSystem(unittest.TestCase):

    def setUp(self):
        # Ініціалізація перед кожним тестом
        global clients
        clients = []
    
    # 1. Тест на додавання клієнта
    def test_add_client(self):
        add_client("Іван Іванов", "Toyota Corolla", "2024-10-25")
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0]['name'], "Іван Іванов")
        self.assertEqual(clients[0]['car_model'], "Toyota Corolla")
        self.assertEqual(clients[0]['service_date'], "2024-10-25")

    # 2. Тест на видалення клієнта
    def test_remove_client(self):
        add_client("Іван Іванов", "Toyota Corolla", "2024-10-25")
        add_client("Марія Коваленко", "Honda Civic", "2024-10-30")
        remove_client("Іван Іванов")
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0]['name'], "Марія Коваленко")
    
    # 3. Тест на отримання всіх клієнтів
    def test_get_all_clients(self):
        add_client("Іван Іванов", "Toyota Corolla", "2024-10-25")
        add_client("Марія Коваленко", "Honda Civic", "2024-10-30")
        all_clients = get_all_clients()
        self.assertEqual(len(all_clients), 2)
    
    # 4. Тест на пошук клієнта
    def test_find_client(self):
        add_client("Іван Іванов", "Toyota Corolla", "2024-10-25")
        client = find_client("Іван Іванов")
        self.assertIsNotNone(client)
        self.assertEqual(client['name'], "Іван Іванов")
    
    # 5. Тест на оновлення інформації про клієнта
    def test_update_client(self):
        add_client("Іван Іванов", "Toyota Corolla", "2024-10-25")
        update_client("Іван Іванов", new_car_model="Toyota Camry", new_service_date="2024-11-01")
        client = find_client("Іван Іванов")
        self.assertEqual(client['car_model'], "Toyota Camry")
        self.assertEqual(client['service_date'], "2024-11-01")

if __name__ == '__main__':
    unittest.main()
