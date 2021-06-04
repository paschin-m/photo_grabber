from bs4 import BeautifulSoup
import urllib.request
import urllib3


def set_current_page_obj(url):
    """
    Функция выцепляет ссылки из HTML-страницы,
    которая скачана в память библиотекой urllib
    и не сильно то и ебен оптимизация! Ваще пахую
    :param url: url-строка говносайта
    :return:  списочек ссылок для СПЫЗЖЫВАНИЯ
    """
    result_href_list = []
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        base_img_url = str(link.get('href'))
        if base_img_url.find('http') > -1:
            result_href_list.append(base_img_url)
        else:
            continue
    print(result_href_list)
    return result_href_list


def save_img(url_img, file_path, counter):
    """
    Тут пЫздять фалы с инторнетов
    :param counter: счетчит СПЫЗЖЕННОГО
    :param file_path: ебаный файл
    :param url_img: ссыль на картинку
    :return: фал с картинкой спызженный
    """
    http = urllib3.PoolManager()
    pic = http.request('GET', url_img)
    with open(str(file_path)+str(f'/{counter}.jpg'), 'wb') as grabber_img:
        grabber_img.write(pic.data)