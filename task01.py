from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def calculate_value(job: PrintJob, max_volume: float) -> float:
    if job.volume > max_volume:
        return 0
    return (max_volume / job.volume + job.volume / job.print_time) / job.priority

def optimize_printing(print_jobs: List[PrintJob], constraints: PrinterConstraints) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """
    # Тут повинен бути ваш код
    print_order = []
    print_tasks = print_jobs.copy()
    total_time = 0
    while len(print_order) < len(print_jobs):
        may_print = constraints.max_items
        max_volume = constraints.max_volume
        cur_time = 0
        while may_print > 0 and len(print_tasks) > 0:
            values = [calculate_value(print_tasks[i], max_volume) for i in range(len(print_tasks))]
            max_value = max(values)
            if max_value == 0:
               break

            max_idx = values.index(max_value)
            may_print -= 1
            curr_job = print_tasks.pop(max_idx)
            max_volume -= curr_job.volume
            cur_time = max([cur_time, curr_job.print_time])
            print_order.append(curr_job)
          
        total_time += cur_time

    return {"print_order": [print_order[i].id for i in range(len(print_order))], "total_time": total_time}


# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        PrintJob("M1", 100, 1, 120),
        PrintJob("M2", 150, 1, 90),
        PrintJob("M3", 120, 1, 150)
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        PrintJob("M1", 100, 2, 120),  # лабораторна
        PrintJob("M2", 150, 1, 90),  # дипломна
        PrintJob("M3", 120, 3, 150)  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        PrintJob("M1", 250, 1, 180),
        PrintJob("M2", 200, 1, 150),
        PrintJob("M3", 180, 2, 120)
    ]

    constraints = PrinterConstraints(300, 2)

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")

if __name__ == "__main__":
    test_printing_optimization()

