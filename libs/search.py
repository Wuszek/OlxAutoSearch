from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def search_by_id(driver, element_id):
    try:
        element = driver.find_element(By.ID, element_id)
        print(f"INFO : Found element {element_id}")
        return element
    except NoSuchElementException as e:
        print(f"ERROR : {e}")
    except ElementClickInterceptedException as e:
        print(f"ERROR : {e}")
    except TimeoutException as t:
        print(f"ERROR : {t}")


def search_by_xpath(driver, element_xpath):
    try:
        element = driver.find_element(By.XPATH, element_xpath)
        print(f"INFO : Found element {element_xpath}")
        return element
    except NoSuchElementException as e:
        print(f"ERROR : {e}")
    except ElementClickInterceptedException as e:
        print(f"ERROR : {e}")
    except TimeoutException as t:
        print(f"ERROR : {t}")


def search_by_css(driver, element_css):
    try:
        element = driver.find_element(By.CSS_SELECTOR, element_css)
        print(f"INFO : Found element {element_css}")
        return element
    except NoSuchElementException as e:
        print(f"ERROR : {e}")
    except ElementClickInterceptedException as e:
        print(f"ERROR : {e}")
    except TimeoutException as t:
        print(f"ERROR : {t}")
