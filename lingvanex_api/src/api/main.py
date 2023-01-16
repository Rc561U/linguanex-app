# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# import json
# import re
# import requests
# import datetime
# from datetime import datetime
#
#
# def get_chrome_driver() -> WebDriver:
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("- incognito")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--window-size=1920,1080")
#     return webdriver.Chrome(options=options)
#
#
# def scrape(driver: WebDriver, url: str, pause: int) -> list:
#     print(type(driver))
#     driver.get(url)
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True and len(driver.find_elements(By.XPATH, "//div[@role='gridcell']//div//a")) < 200:
#         # Scroll down to bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         # Wait to load page
#         time.sleep(pause)
#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#
#         if new_height == last_height: break
#         last_height = new_height
#
#         print(len(driver.find_elements(By.XPATH, "//div[@role='gridcell']//div//a")))
#
#     return driver.find_elements(By.XPATH, "//div[@role='gridcell']//div//a")
#
#
# def record(collection):
#     for i, webElement in enumerate(collection):
#         with open("ids.txt", "a", newline="") as file:
#             # zalupa.append(webElement.get_attribute("href").split("/")[-1])
#             ids = webElement.get_attribute("href").split("/")[-1]
#             file.write(ids + "\n")
#
#
# ###
# def getAllInfo(datajson: dict) -> dict:
#     return {
#         "App name": datajson["title"] if datajson["title"] else 'No title',
#         "Company name": datajson["publisherName"] if datajson["publisherName"] else 'No publisher',
#         "Release date": datetime.fromisoformat(datajson[
#                                                    "releaseDateUtc"]).strftime("%Y-%m-%d") if datajson[
#             "releaseDateUtc"] else 'No release date',
#         "Email": checkEmail(datajson["supportUris"][0]['uri']) if checkEmail(
#             datajson["supportUris"][0]['uri']) else 'No email',
#     }
#
#
# def checkEmail(email):
#     if not email: return False
#     regex = r"((?!mailto:))\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
#     if re.search(regex, email):
#         return re.search(regex, email).group(0)
#     else:
#         return False
#
# def get_information(url: str):
#     application_row = requests.get(url)
#     return application_row.json()
#
#
# def record_data_to_json(data):
#     with open("result.json", "w") as jsonfile:
#         json.dump(data, jsonfile, indent=4, ensure_ascii=False)
#
#
# def save_product_by_id(json_data):
#
#     print(json_data["title"] if json_data["title"] else 'No title')
#     print(json_data["publisherName"] if json_data["publisherName"] else 'No publisher')
#     print(datetime.fromisoformat(json_data[
#                                              "releaseDateUtc"]).strftime("%Y-%m-%d") if json_data[
#         "releaseDateUtc"] else 'No release date')
#     print(checkEmail(json_data["supportUris"][0]['uri']) if checkEmail(
#         json_data["supportUris"][0]['uri']) else 'No email')
#
#
# def get_product_by_id(product_id):
#     url = f'https://apps.microsoft.com/store/api/ProductsDetails/GetProductDetailsById/{product_id}'
#     product_json = requests.get(url)
#     text = product_json.json()
#
#     save_product_by_id(text)
#     print()
#
#
# def main():
#     url = "https://apps.microsoft.com/store/category/Business"
#     timer = 5
#     driver = get_chrome_driver()
#
#     elements_collection = scrape(driver, url, timer)
#
#     for webElement in elements_collection:
#         ids = webElement.get_attribute("href").split("/")[-1]
#     # record(elements_collection)
#         # loop(file)
#         get_product_by_id(ids)
#
#
# if __name__ == "__main__":
#     main()
#
#

from celery import shared_task
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import json
import re
import requests
import datetime
from datetime import datetime
from .models import Application


@shared_task
def get_chrome_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("- incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


@shared_task
def scrape(driver: WebDriver, url: str, pause: int) -> list:
    print(type(driver))
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True and len(driver.find_elements(By.XPATH, "//div[@role='gridcell']//div//a")) < 200:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(pause)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height: break
        last_height = new_height

        print(len(driver.find_elements(By.XPATH, "//div[@role='gridcell']//div//a")))

    return driver.find_elements(By.XPATH, "//div[@role='gridcell']//div//a")


@shared_task
def record(collection):
    for i, webElement in enumerate(collection):
        with open("ids.txt", "a", newline="") as file:
            # zalupa.append(webElement.get_attribute("href").split("/")[-1])
            ids = webElement.get_attribute("href").split("/")[-1]
            file.write(ids + "\n")


@shared_task
def getAllInfo(datajson: dict) -> dict:
    return {
        "App name": datajson["title"] if datajson["title"] else 'No title',
        "Company name": datajson["publisherName"] if datajson["publisherName"] else 'No publisher',
        "Release date": datetime.fromisoformat(datajson[
                                                   "releaseDateUtc"]).strftime("%Y-%m-%d") if datajson[
            "releaseDateUtc"] else 'No release date',
        "Email": checkEmail(datajson["supportUris"][0]['uri']) if checkEmail(
            datajson["supportUris"][0]['uri']) else 'No email',
    }


@shared_task
def checkEmail(email):
    if not email: return False
    regex = r"((?!mailto:))\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.search(regex, email):
        return re.search(regex, email).group(0)
    else:
        return False


@shared_task
def get_information(url: str):
    application_row = requests.get(url)
    return application_row.json()


@shared_task
def record_data_to_json(data):
    with open("result.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


@shared_task
def save_product_by_id(json_data):
    Application.objects.get_or_create(
        title=json_data["title"] if json_data["title"] else 'No title',
        publisher=json_data["publisherName"] if json_data["publisherName"] else 'No publisher',
        publishedYear=datetime.fromisoformat(json_data[
                                                 "releaseDateUtc"]).strftime("%Y-%m-%d") if json_data[
            "releaseDateUtc"] else 'No release date',
        email=checkEmail(json_data["supportUris"][0]['uri']) if checkEmail(
            json_data["supportUris"][0]['uri']) else 'No email',
    )


@shared_task
def get_product_by_id(product_id):
    url = f'https://apps.microsoft.com/store/api/ProductsDetails/GetProductDetailsById/{product_id}'
    product_json = requests.get(url)
    text = product_json.json()

    save_product_by_id(text)
    print(f'Save product => {url}')


@shared_task
def main():
    url = "https://apps.microsoft.com/store/category/Business"
    timer = 5
    driver = get_chrome_driver()

    elements_collection = scrape(driver, url, timer)

    for webElement in elements_collection:
        ids = webElement.get_attribute("href").split("/")[-1]
        get_product_by_id(ids)
    print('Done successfully!')


if __name__ == "__main__":
    main()
