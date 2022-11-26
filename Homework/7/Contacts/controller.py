import view
import model
from tabulate import tabulate

txt = 'Нажмите enter чтобы продолжить...'
action_name = None


def start():
    global action_name
    view.get_data("Вас приветствует Первый ТЕЛЕФОННЫЙ Справочник\n"
                  "Для начала работы нажмите enter")
    while True:
        sel_opt = model.start_list()
        match sel_opt:
            case "1":
                action_name = view.get_data("Введите имя файла, который хотите загрузить\n")
                if model.load_db(action_name):
                    view.get_data(f"Справочник {action_name} загружен\n" + txt)
                else:
                    view.get_data("Файла с таким именем нет\n" + txt)
            case "2":
                action_name = view.get_data('Введите имя для файла справочника\n')
                model.save_db(action_name)
                view.get_data(f"Справочник {action_name} сохранён\n" + txt)
            case "3":
                action_name = view.get_data("Введите имя файла, который хотите удалить\n")
                if model.delete_db(action_name):
                    view.get_data(f"Файл {action_name} удалён\n" + txt)
                else:
                    view.get_data("Файла с таким именем нет\n" + txt)
            case "4":
                model.clear_db()
                view.get_data(f"Справочник очищен\n" + txt)
            case "5":
                if not len(model.data.count('columns')):
                    view.get_data('Справочник пуст. Создайте новый или загрузите\n' + txt)
                    continue
                view.show_info(tabulate(model.data, headers='keys', tablefmt='psql'))
                view.get_data(txt)
            case "6":
                action_name = view.get_data("Введите ФИО\n")
                fio = model.add_fio(action_name)
                phone_number = view.get_data("Введите номер телефона\n ")
                model.add_field(fio, phone_number)
                view.get_data(f"В справочник добавлена запись\n" + txt)
            case "7":
                view.show_info(tabulate(model.data, headers='keys', tablefmt='psql'))
                action_name = int(view.get_data("Выберите номер записи, которую хотите удалить\n"))
                model.delete_field(action_name)
                view.get_data(f"Запись номер {action_name} удалена\n" + txt)
            case "8":
                action_name = view.get_data('Введите текст для поиска\n')
                f_string = model.search(action_name)
                view.show_info(f_string)
                view.get_data(txt)
            case "9":
                view.show_info('Шас я отредактирую')
                view.get_data(txt)
            case "0":
                view.show_info("Пока-пока")
                return
            case _:
                view.get_data('Неверный выбор, нажмите enter, чтобы попробовать еще раз')
