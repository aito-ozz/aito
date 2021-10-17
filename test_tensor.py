from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestTensorSearch():
    def test_tensor_search(self, browser):

        # Определяем ссылку и открываем ее в Google Chrome
        link = "https://yandex.ru/"
        browser.get(link)
        browser.implicitly_wait(10)

        # Проверяем наличие поля поиска
        wait = WebDriverWait(browser, 10)
        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'input__control.input__input.mini-suggest__input')))

        # Определяем поле для поиска и вводим запрос
        input1 = browser.find_element_by_class_name("input__control.input__input.mini-suggest__input")
        input1.send_keys("Тензор")

        # Проверяем появилась ли таблица с подсказками
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'mini-suggest__popup-content')))

        # Имитируем нажатие клавиши Enter
        input1.send_keys("\n")

        # Получаем список ссылок на сайты по нашему поисковому запросу
        page_item = browser.find_elements(By.XPATH, '//li[@class="serp-item desktop-card"]//h2/a[@href]')

        # Среди первых пяти ссылок ищем наш сайт
        for i in range(5):
            if page_item[i].get_attribute('href') in 'https://tensor.ru/':
                print('Сайт компании Тензор стоит на', i + 1, 'месте в поисковом запросе')
                break
            else:
                print('Такого сайта нет в первых 5 ссылках')


class TestTensorImage():

    def test_tensor_image(self, browser):
        # Определяем ссылку и открываем ее в Google Chrome
        link = "https://yandex.ru/"
        browser.get(link)

        browser.implicitly_wait(10)

        # Находим кнопку "Картинки" и кликаем на нее
        button_img = browser.find_element_by_tag_name('[data-id="images"]')  #
        button_img.click()

        # Переходим на открывшуюся вкладку "Картинки"
        img_page = browser.window_handles[1]
        browser.switch_to.window(img_page)

        # Проверяем, открылась ли нужная ссылка
        assert 'https://yandex.ru/images/' in browser.current_url, 'Открыта неверная страница.'

        # Находим первый элемент, его заголовок и кликаем на элемент
        first_request = browser.find_element_by_class_name('PopularRequestList-Item.PopularRequestList-Item_pos_0')
        first_request_text = browser.find_element_by_xpath(
            '//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"] //div['
            '@class="PopularRequestList-SearchText"]').text
        first_request.click()

        # Проверяем совпадает ли заголовок страницы с заголовком элемента
        wait = WebDriverWait(browser, 10)
        search_query_text = wait.until(EC.title_contains(first_request_text))

        # Находим первое изображение, его ссылку в виде списка, для сравнения, и кликаем на изображение
        first_img = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a')
        first_img_url = \
            browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a[@href]').get_attribute(
                'href').split('&pos=')[-1]
        first_img.click()

        # В открывшейся карусели находим ссылку на источник изображения
        in_first_img_url = browser.find_element_by_xpath(
            '/html/body/div[11]/div[1]/div/div/div[3]/div/div[3]/div/div/div[1]/div/div[1]/a').get_attribute('href')

        # Получаем ссылку текущей страницы/карусели в виде списка, для сравнения
        current_page = str(browser.current_url).split('&pos=')[-1]

        # Сравниваем ссылку на первое изображение и ссылку изображения из карусели
        assert current_page in first_img_url, 'Открылось неверное изображение'

        # Кликаем по кнопке прокрутки карусели, для смены избражения на следующее
        browser.find_element_by_xpath('/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]/i').click()

        # Получаем ссылку на источник второго изображения из карусели
        in_second_img_url = browser.find_element_by_xpath(
            '/html/body/div[11]/div[1]/div/div/div[3]/div/div[3]/div/div/div[1]/div/div[1]/a').get_attribute('href')

        # Сравниваем первое и второе изображения
        assert in_first_img_url != in_second_img_url, 'Изображение не изменилось'

        # Кликаем на кнопку для возвращения к предыдущему изображению
        browser.find_element_by_xpath('/html/body/div[11]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]/i').click()

        # Получаем ссылку на источник изображения из карусели
        in_last_img_url = browser.find_element_by_xpath(
            '/html/body/div[11]/div[1]/div/div/div[3]/div/div[3]/div/div/div['
            '1]/div/div[1]/a').get_attribute('href')

        # Сравниваем ссылку на источник первого изображения и последнего
        assert in_last_img_url == in_first_img_url, 'Это не то изображение, которое было изначально'

