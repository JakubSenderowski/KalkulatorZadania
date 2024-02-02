def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Nie można dzielić przez zero!"
    return x / y

# Przykład użycia
if __name__ == "__main__":
    print("Wybierz operację:")
    print("1.Dodawanie")
    print("2.Odejmowanie")
    print("3.Mnożenie")
    print("4.Dzielenie")

    choice = input("Wpisz numer operacji (1/2/3/4): ")

    num1 = float(input("Wpisz pierwszą liczbę: "))
    num2 = float(input("Wpisz drugą liczbę: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Niepoprawny wybór")
