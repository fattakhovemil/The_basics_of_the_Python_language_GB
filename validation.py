def valid_amount(amount):
    while True:  # вадидация при создании объекта
        try:
            amount = int(amount)
            if amount <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print(f"Ошибка при создании объекта")
            amount = int(input("Введите корректное количество товара (целое, положительное)\n"))
    return amount


def valid_price(price):
    while True:  # вадидация при создании объекта
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print(f"Ошибка при создании объекта")
            price = float(input("Введите корректную цену товара (положительное число)\n"))
    return price