## 1. add path of dir "cloud_cover" to PYTHPNPATH env var.
## set PYTHONPATH=C:\pycharm_ws\project\cloud_cover
## 2. install all packages from requirements.txt
## 3. Command to run :
## pytest --html="../output/report.html" --self-contained-html --log-level INFO
from selenium import webdriver
import logging
from src import consts as CONST

BASE_URL = "https://stackoverflow.com/"
log = logging.getLogger(__name__)


def test_third_tag_and_get_total_questions():
    ## provide Path of chrome driver in PATH env variable.
    driver = webdriver.Chrome(CONST.CHROME_DRIVE_PATH)
    driver.maximize_window()
    driver.get(BASE_URL)
    driver.find_element_by_class_name("left-sidebar-toggle").click()
    driver.find_element_by_xpath('//*[@id="nav-tags"]').click()
    tag_name = driver.find_element_by_xpath('//*[@id="tags-browser"]/div[3]/div[1]/div/a').text
    log.info("Third most popular tag name: {}".format(tag_name))
    driver.find_element_by_xpath('//*[@id="tags-browser"]/div[3]/div[1]/div/a').click()
    no_of_questions = driver.find_element_by_xpath('//*[@id="mainbar"]/div[4]/div/div[1]').text
    log.info("Total number of Questions: {}".format(no_of_questions))
    driver.close()
