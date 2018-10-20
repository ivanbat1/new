# coding: utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "app": r"C:/Program Files (x86)/InstaTrader/terminal.exe"    })

driver.find_element_by_name('USDCHF,H4').click()
ActionChains(driver).send_keys( u'\ue00a').perform()
