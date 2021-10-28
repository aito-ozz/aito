from selenium import webdriver
import pytest
import time


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestEtagiSearch():
    def test_etagi_search(self, browser):

        # Определяем ссылку и открываем ее в Google Chrome
        # browser = webdriver.Chrome()
        link = "https://www.etagi.com/"
        browser.get(link)
        browser.implicitly_wait(10)

        # Выбираем 1 комнату
        rooms = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div/button[2]")
        rooms.click()

        # Указываем ценовой диапазон от 1.000.000 до 3.000.000
        # От:
        from_x = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div/input")
        from_x.send_keys('1000000')
        # До:
        to_y = browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/div/input")
        to_y.send_keys("3000000")
        time.sleep(2)

        # Нажимаем Найти
        search = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/a")
        search.click()

        time.sleep(2)

        # Находим квартиры, проверяем цену и количество комнат на превью и собираем ссылки на них
        apartments = browser.find_elements_by_xpath("//div/span/a[@target]")

        ap_list = []

        cost = browser.find_elements_by_xpath("//div/span[@class='_1s0Jo _2Ylcq']")

        for j in range(3):
            for i in range(len(apartments)):
                ap_list.append(apartments[i].get_attribute("href"))
                if (apartments[i].text == "1-комн. квартира") and (1000000 <= int(cost[i].text.replace(" ",
                                                                                                       "")) <= 3000000):
                    continue
                else:
                    print(apartments[i].get_attribute("href"), "- Квартира не подходит")

            time.sleep(2)
            next_page_button = browser.find_element_by_class_name("MeZ1D.Z4Tdx.Nluev.t7k6n._1Yxi5")
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next_page_button.click()
            print(len(ap_list))

        # Проверяем каждую страницу каждой квартиры
        for i in ap_list:
            browser.get(i)
            rooms_x = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/span").text
            cost_x = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div["
                "1]/div[1]/span").text.replace(" ", "")
            if "1-комн. квартира" in rooms_x and (1000000 <= int(cost_x) <= 3000000):
                continue
            else:
                print(i, "- Квартира не подходит")
