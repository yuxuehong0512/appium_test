# author_='Yuxuehong';
# date: 2023/8/17 16:38
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def wait_clickable(d, b, v):
    l_ = (b, v)
    return WebDriverWait(d, 10).until(EC.element_to_be_clickable(l_))


def wait_visibility(d, b, v):
    l_ = (b, v)
    return WebDriverWait(d, 10).until(EC.visibility_of_element_located(l_))


def wait_visibility_all(d, b, v):
    l_ = (b, v)
    return WebDriverWait(d, 10).until(EC.visibility_of_all_elements_located(l_))