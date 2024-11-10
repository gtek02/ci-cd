# main.py

from calculator import add, subtract, multiply, divide

def main():
    print("Witaj w kalkulatorze! Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    choice = input("Wybierz operację (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print(f"Wynik: {add(a, b)}")
        elif choice == '2':
            print(f"Wynik: {subtract(a, b)}")
        elif choice == '3':
            print(f"Wynik: {multiply(a, b)}")
        elif choice == '4':
            try:
                print(f"Wynik: {divide(a, b)}")
            except ValueError as e:
                print(e)
    else:
        print("Niepoprawny wybór!")

if __name__ == "__main__":
    main()
