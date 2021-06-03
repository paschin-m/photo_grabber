import os
import pathlib

PROTOCOL = 'http'
ALIAS_SEPARATOR = '/'


def set_dir_struct(alias):
    """
    идет на вход строка, из которой
    иерархически вырезаются имена вложенных каталогов
    каталоги создаются используя модуль ос и верифицируется
    сама полученная структура путем вложенного обхода
    :param alias:  строка с разделением '/' в url
    :return: суммарный код завершения 0-все успешно
    """
    if len(str(alias)) < 3:
        print(f'Херовая строка, мало букав')
    lst_dirs = str(alias).replace('/', ' ').split()
    base_name=pathlib.Path.cwd()
    os.mkdir(f'{base_name.joinpath(lst_dirs[3])}')
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
    return 0
