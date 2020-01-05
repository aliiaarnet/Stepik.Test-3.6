import selenium
from selenium import webdriver
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_existence(browser):
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button>0, "THE BUTTON DOESN'T EXIST"
    time.sleep(10)
