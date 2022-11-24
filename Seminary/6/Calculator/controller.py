import model
import view


def start():
    view.show_info("Привет, я калькулятор")
    a = view.get_numb("Введите первое число ")
    b = view.get_numb("Введите второе число ")
    model.init(a, b)

    check = view.get_numb("""
Выберите операцию    
    1 - Сложение
    2 - Вычитание
    3 - Умножение
    4 - Деление    
""")
    result = None
    match check:
        case '1':
            result = model.summa_op()
        case '2':
            result = model.subtract_op()
        case '3':
            result = model.multiply_op()
        case '4':
            result = model.division_op()
        case _:
            result = "Нет такого действия"

    view.show_info(result)


print(bin(1))