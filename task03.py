import heapq

def min_cost_to_connect_cables(cable_lengths):
    '''Обчислює мінімальні витрати на з'єднання всіх мережевих кабелів'''

    if len(cable_lengths) < 2:
        return 0
    
    # Перетворюємо список на мін-купу
    heapq.heapify(cable_lengths)

    total_cost = 0

    # Продовжуємо, поки в купі не залишиться один (фінальний) кабель
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротші кабелі.
        first_shortest = heapq.heappop(cable_lengths)
        second_shortest = heapq.heappop(cable_lengths)

        # Вартість поточного з'єднання.
        cost = first_shortest + second_shortest
        
        # Додаємо цю вартість до загальної суми.
        total_cost += cost

        # Кладемо новий, об'єднаний кабель назад у купу.
        heapq.heappush(cable_lengths, cost)

    return total_cost

if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    min_cost = min_cost_to_connect_cables(list(cables))
    print(f"Довжини кабелів: {cables}")
    print(f"Мінімальні витрати на з'єднання: {min_cost}")

    print("-" * 20)

    cables2 = [20, 4, 8, 2]
    min_cost2 = min_cost_to_connect_cables(list(cables2))
    print(f"Довжини кабелів: {cables2}")
    print(f"Мінімальні витрати на з'єднання: {min_cost2}")

    print("-" * 20)

    cables3 = [1, 2, 3, 4, 5]
    min_cost3 = min_cost_to_connect_cables(list(cables3))
    print(f"Довжини кабелів: {cables3}")
    print(f"Мінімальні витрати на з'єднання: {min_cost3}")