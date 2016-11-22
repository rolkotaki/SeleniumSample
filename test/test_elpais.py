from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class TestElPais:

    def setup(self):
        # self.driver = webdriver.Remote("http://192.168.99.100:33333/wd/hub", DesiredCapabilities.CHROME.copy())
        self.driver = webdriver.Firefox()
        self.driver.get("http://elpais.com/")

    def test_elpais(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='cabecera-seccion']/div/div[2]/div/nav/ul/li[3]/a").click()
        driver.find_element_by_id("boton_buscador").click()
        driver.find_element_by_name("qt").send_keys("partido popular")
        driver.find_element_by_name("qt").send_keys(Keys.RETURN)

        time.sleep(3)
        self.assertTrue(1==1)

    def teardown(self):
        self.driver.quit()