def check():
    x = int(input("Введите натуральное число x: "))
    y = int(input("Введите натуральное число y: "))

    if x % y == 0:
        print(f"{x} делится нацело на {y}.")
    else:
        print(f"{x} не делится нацело на {y}.")

if __name__ == "__main__":
    check()