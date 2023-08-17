# author_='Yuxuehong';
# date: 2023/8/17 16:38

from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

def Wait_visibity(d, b, v):
    l_ = (b, v)
    return Wait(d, 10).until(EC.visibility_of_element_located(l_))


def Wait_visibity_all(d, b, v):
    l_ = (b, v)
    return Wait(d, 10).until(EC.visibility_of_all_elements_located(l_))