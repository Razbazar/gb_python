import os.path
import pandas as pd
import os
from controller import *

data = pd.DataFrame(columns=['Фамилия', 'Имя', 'Отчество', 'Телефон'])


def start_list():
    return view.get_data('''
1 - Загрузить справочник
2 - Сохранить справочник
3 - Удалить справочник
4 - Очистить справочник
5 - Показать справочник
6 - Добавить запись
7 - Удалить запись  
8 - Найти запись
9 - Редактировать запись
0 - Выйти 
''')


def load_db(file_to_load):
    global data
    try:
        data = pd.read_csv(file_to_load + '.csv')
        return True
    except FileNotFoundError:
        return


def save_db(file_to_save):
    data.index += 1
    data.to_csv(file_to_save + '.csv', index=False)


def delete_db(file_to_delete):
    try:
        os.remove(file_to_delete + '.csv')
        return True
    except FileNotFoundError:
        return


def clear_db():
    data.drop(data.index, inplace=True)


def add_fio(fio_param):
    fio_text = fio_param.split()
    txt_len = 3 - len(fio_text)
    fio_text.extend([' '] * txt_len)
    return fio_text


def add_field(fio_param, phone):
    fio_param.append(phone)
    data.loc[-1] = fio_param
    data.reset_index(drop=True, inplace=True)


def delete_field(field_to_delete):
    data.drop(field_to_delete, inplace=True)
    data.reset_index(drop=True, inplace=True)


def search(text_to_search):
    return data[data.apply(lambda row: row.astype(str).str.contains(text_to_search, case=False).any(), axis=1)]