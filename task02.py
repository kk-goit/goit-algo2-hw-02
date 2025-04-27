from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int], memo: List) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
		# Тут повинен бути ваш код
    answ = {
        "max_profit": 0,
        "cuts": [],
        "number_of_cuts": 0
    }

    if length == 0:
        return answ 

    if not memo[length - 1] is None:
        return memo[length - 1]

    for j in range(1, length + 1):
        curr = rod_cutting_memo(length - j, prices, memo)
        profit = prices[j - 1] + curr['max_profit']

        if profit > answ["max_profit"]:
          answ = curr.copy()
          answ['max_profit'] = profit
          answ['cuts'] = [j] + curr['cuts']

    answ['number_of_cuts'] = len(answ['cuts']) - 1
    memo[length - 1] = answ
    return answ

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    # Тут повинен бути ваш код
    table = [{"max_profit": 0, "cuts": [], "number_of_cuts": 0} for i in range(length + 1)]

    for i in range(1, length + 1):
      answ = {
          "max_profit": 0,
          "cuts": [],
          "number_of_cuts": length - 1
      }
      for j in range(1, i + 1):
        profit = prices[j - 1] + table[i - j]['max_profit']
        if profit > answ["max_profit"]:
          answ['max_profit'] = profit
          answ['cuts'] = table[i - j]['cuts'] + [j]

      answ['number_of_cuts'] = len(answ['cuts']) - 1
      table[i] = answ

    return table[length]

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
        # """
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo = [None for i in range(test['length'])]
        memo_result = rod_cutting_memo(test['length'], test['prices'], memo)
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
