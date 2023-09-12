from faker import Faker
import random
import time
import psutil
import csv

fake = Faker()  # O(1)


def generate_data():
    data = []
    # la complejidad de buble principal es O(n^2)
    for _ in range(500**2):
        username = fake.user_name()  # O(1)
        birthdate = fake.date_of_birth(
            minimum_age=18,
            maximum_age=70).strftime('%Y-%m-%d')  # O(1)
        income = round(random.uniform(1000, 10000), 2)  # O(1)
        debt = round(random.uniform(0, 5000), 2)  # O(1)
        sex = random.choice(['Male', 'Female'])  # O(1)
        num_children = random.randint(0, 5)  # O(1)
        country = fake.country()  # O(1)
        data.append([
            username,
            birthdate,
            income,
            debt,
            sex,
            num_children,
            country])

    return data


def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)  # O(1)
        writer.writerow([
            'Username',
            'Birthdate',
            'Income',
            'Debt',
            'Sex',
            'Number of Children',
            'Country'])  # O(1)
        writer.writerows(data)  # O(n^2)


if __name__ == "__main__":
    start_time = time.time()  # O(1)
    memoria_inicio = psutil.virtual_memory().used  # O(1)
    generated_data = generate_data()  # O(n^2)
    save_to_csv(generated_data, 'dummy_data.csv')  # O(n^2)
    print("Data generation and CSV creation complete.")
    end_time = time.time()  # O(1)
    memoria_fin = psutil.virtual_memory().used  # O(1)
    diferencia_memoria = abs(memoria_fin - memoria_inicio)  # O(1)

    print(end_time - start_time)  # O(1)
    print(f"la diferencia de memoria utilizada es: {diferencia_memoria} bytes")  # O(1)



                            # BIG- O DEL CODIGO: O(n^2)
