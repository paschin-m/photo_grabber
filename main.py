import dir_func
import os
import pathlib
import site_parser
'''
 Это скрипт из РОССИИ и ХУЙ тут будут на ебаном буржуйском коменты.
 Более того, я как автор данного поделья КЛАЛ хуи на всех недоумков,
которые будут копировать данную поеботу. Мамкины программЫсты я ваш
рот ЕБ. Мне похуй на безопасность и все сообщесто быдлокодеров и
кодеров питона в особенности. Я ебал и вертел на хуй ВСЕ ваши
языки стандарты и само ИТ в рот ЕБ. Срал и ебал всех ИТшников.
ИТшники - вы все говноеды и ебаные пиздюки, ссал вам всем в рты.
'''


def print_hi(name):
    """
    здесь надо насрать что-то умное, но мне поебать
    я и так пиздат и под вискарем ебал все в рот!!!
    :param name: поебень какая-то
    :return: хуйня
    """
    print(f'"Эт интернеты ептать, {name}')


# Ебись все колом, поселось говно по трубам
if __name__ == '__main__':
    print_hi('ИДИ НА ХУЙ!')
    name_dir = pathlib.Path.cwd().joinpath(f'ХУЙ')
    os.mkdir(name_dir)
    for c in range(1, 10, 1):
        url = f'http://хуемаЁ/{c}/'
        os.mkdir(name_dir.joinpath(f'{c}'))
        dr = name_dir.joinpath(f'{c}')
        links = site_parser.set_current_page_obj(url)
        k = 0
        for ln in links:
            site_parser.save_img(ln, dr, k)
            k += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
