from selenium.webdriver.common.by import By


class Locators:
    find_contacts = [By.LINK_TEXT, 'Контакты']
    find_banner = [By.XPATH, "//a[@title='tensor.ru']"]
    find_blocks = [By.CLASS_NAME, 'tensor_ru-content_wrapper']
    find_block_work = [By.XPATH, "//*[contains(text(), 'Работаем')]/../.."]
    find_img = [By.TAG_NAME, 'img']
    button_more = [By.XPATH, "//*[contains(text(), 'Сила в людях')]/parent::div/child::p/child::*[contains(text(), 'Подробнее')]"]
    region_name = [By.CLASS_NAME, 'sbis_ru-Region-Chooser__text']
    list_partner = [By.XPATH, "//div[@id='contacts_list']/descendant::div[@data-qa='item']"]
    kamchatka_click = (By.XPATH, "//span[@title='Камчатский край']")
