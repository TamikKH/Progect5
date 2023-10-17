def animals():
    for bulls in range(0, 101):
        for cows in range(0, 101):
            for calves in range(0, 101):
                if bulls + cows + calves == 100 and 10 * bulls + 5 * cows + 0.5 * calves == 100:
                    return bulls, cows, calves
    return None

result = animals()
if result:
    bulls, cows, calves = result
    print(f"Количество быков:",bulls, "количество коров:", cows, "количество телят:", calves)
else:
    print("Решение не найдено.")