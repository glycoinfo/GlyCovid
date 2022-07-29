import time
import traceback
import re
import os
import copy
import sys
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from training import shadowing
from accounts import learner


# https://qiita.com/motoki1990/items/a59a09c5966ce52128be
def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--use-fake-device-for-media-stream')
    options.add_argument('--use-fake-ui-for-media-stream')
    options.add_argument('--use-fake-device-for-media-stream')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # assert "Python" in driver.title
    try:
        driver.get('http://localhost:3030/dataset.html')
        learner.main(driver)
        shadowing.main(driver)

    except:
        traceback.print_exc()
        driver.quit()
        return
    finally:
        driver.quit()
        return


if __name__ == "__main__":
    main()
