import math

def calculate_triangle_area(side_a, side_b, angle_degrees):
    """
    Вычисляет площадь треугольника по двум сторонам и углу между ними.
    
    Параметры:
    side_a, side_b - длины сторон в сантиметрах
    angle_degrees - угол между сторонами в градусах
    
    Возвращает:
    площадь треугольника в квадратных сантиметрах
    """
    # Преобразуем угол из градусов в радианы
    angle_radians = math.radians(angle_degrees)
    
    # Вычисляем площадь по формуле: S = 1/2 * a * b * sin(C)
    area = 0.5 * side_a * side_b * math.sin(angle_radians)
    
    return area

def main():
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ ВЫЧИСЛЕНИЯ ПЛОЩАДИ ТРЕУГОЛЬНИКА")
    print("По двум сторонам и углу между ними")
    print("=" * 50)
    
    try:
        # Ввод данных от пользователя
        side_a = float(input("Введите длину первой стороны (в см): "))
        side_b = float(input("Введите длину второй стороны (в см): "))
        angle = float(input("Введите угол между сторонами (в градусах): "))
        
        # Проверка корректности введенных данных
        if side_a <= 0 or side_b <= 0:
            print("Ошибка: Длины сторон должны быть положительными числами!")
            return
        
        if angle <= 0 or angle >= 180:
            print("Ошибка: Угол должен быть больше 0 и меньше 180 градусов!")
            return
        
        # Вычисление площади
        area = calculate_triangle_area(side_a, side_b, angle)
        
        # Вывод результата
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТ ВЫЧИСЛЕНИЙ:")
        print(f"Сторона a = {side_a} см")
        print(f"Сторона b = {side_b} см")
        print(f"Угол между сторонами = {angle}°")
        print(f"Площадь треугольника = {area:.2f} кв. см")
        print("=" * 50)
        
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные числовые значения!")

if __name__ == "__main__":
    main()