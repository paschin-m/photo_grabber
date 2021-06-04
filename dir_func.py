import os
import pathlib

PROTOCOL = 'http'
ALIAS_SEPARATOR = '/'


def set_dir_struct(alias):
    """
    @TODO на кой хуй это говно надо?!
    идет на вход строка, из которой
    иерархически вырезаются имена вложенных каталогов
    каталоги создаются используя модуль ос и верифицируется
    сама полученная структура путем вложенного обхода
    :param alias:  строка с разделением '/' в url
    :return: суммарный код завершения 0-все успешно
    """
    result_lst = []
    if len(str(alias)) < 3:
        print(f'Херовая строка, мало букав')
    lst_dirs = str(alias).replace('/', ' ').split()
    base_name = pathlib.Path.cwd()
    if os.path.exists(f'{base_name.joinpath(lst_dirs[3])}'):
        result_lst.append(f'{base_name.joinpath(lst_dirs[3]).joinpath(lst_dirs[4])}')
        os.mkdir(f'{base_name.joinpath(lst_dirs[3]).joinpath(lst_dirs[4])}')
    else:
        os.mkdir(f'{base_name.joinpath(lst_dirs[3])}')
        os.mkdir(f'{base_name.joinpath(lst_dirs[3]).joinpath(lst_dirs[4])}')
        result_lst.append(f'{base_name.joinpath(lst_dirs[3]).joinpath(lst_dirs[4])}')
    '''
    @TODO ебани динамики на каталоги, хуле ты ебешь мозг
    for dr in lst_dirs:
        name = base_name.joinpath(f'{dr}')
        if os.path.exists(name):
            name = name.joinpath(f'{dr}')
            os.mkdir(name)
        else:
            os.mkdir(name)
        print(dr)
    '''
    return result_lst
