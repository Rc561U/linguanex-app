from celery import shared_task
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import json
import re
import requests
import datetime
from datetime import datetime
from .models import Application


# @shared_task
# def get_chrome_driver() -> WebDriver:
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("- incognito")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--window-size=1920,1080")
#     time.sleep(5)
#     driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME,
#                             options=options)
#     driver.get('https://python.org')
#     driver.save_screenshot('screenshot.png')
#     return driver


@shared_task
def save_product_by_id():
    Application.objects.get_or_create(
        title="Test",
        publisher="Poloes",
        publishedYear=1232,
        email='mail@mail.cim',
    )
