from selenium import webdriver
import pytest
from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from pages.locators import Locators


@pytest.fixture()
def browser():
    chrome = webdriver.Chrome()
    return chrome


def test_scenario_1(browser):
    obj = BasePage(browser, 'https://sbis.ru/')
    obj.to_site()
    obj.find_element(Locators.find_contacts).click()
    obj.find_element(Locators.find_banner).click()
    obj.get('https://tensor.ru/')
    block = obj.find_element(Locators.find_blocks)
    assert 'Сила в людях' in block.text

    about = block.find_element(*Locators.button_more)
    assert about.get_attribute('href') == 'https://tensor.ru/about'

    obj.get(about.get_attribute('href'))
    block_work = obj.find_element(Locators.find_block_work)
    array_img = block_work.find_elements(*Locators.find_img)
    w = array_img[0].get_attribute('width')
    h = array_img[0].get_attribute('height')
    for img in array_img:
        assert img.get_attribute('width') == w
        assert img.get_attribute('height') == h
    obj.browser.quit()

def test_scenario_2(browser):
    obj = BasePage(browser, 'https://sbis.ru/')
    obj.to_site()
    obj.find_element(Locators.find_contacts).click()
    region = obj.wait_click_element(Locators.region_name)
    assert region.text == 'Владимирская обл.'
    text_partner = []
    try:
        block_partner = obj.get_array_elements(Locators.list_partner)
        for i in block_partner:
            text_partner.append(i.text)
    except NoSuchElementException:
        print('no such elements')

    region.click()
    obj.wait_click_element(Locators.kamchatka_click).click()
    obj.wait_text_element(Locators.region_name, 'Камчатский край')
    assert obj.find_element(Locators.region_name).text == 'Камчатский край'
    block_partner_new = obj.get_array_elements(Locators.list_partner)
    text_partner_new = []
    for i in block_partner_new:
        text_partner_new.append(i.text)
    assert text_partner != text_partner_new
    assert '41-kamchatskij-kraj' in obj.browser.current_url
    assert region.text in obj.browser.title
    obj.browser.quit()
