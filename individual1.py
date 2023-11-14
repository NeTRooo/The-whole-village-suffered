def calculate_earnings(kg_collected):
    if kg_collected <= 50:
        earnings = kg_collected * 0.30  # 30 копеек за 1 кг
    elif 50 < kg_collected <= 75:
        earnings = kg_collected * 0.50  # 50 копеек за 1 кг
    elif 75 < kg_collected <= 90:
        earnings = kg_collected * 0.65  # 65 копеек за 1 кг
    else:
        earnings = kg_collected * 0.70 + 20  # 70 копеек за 1 кг + 20 рублей премии

    return earnings

if __name__ == "__main__":
    kg_collected = float(input("Введите количество килограммов помидоров, собранных студентом: "))
    earnings = calculate_earnings(kg_collected)
    print(f"Заработок студента составил {earnings:.2f} рублей.")
