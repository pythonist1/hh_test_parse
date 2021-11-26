from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
import time
import json
import pickle
# from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
# options = Options()
# options.add_argument("--user-data-dir=chrome-data")
# options.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://hh.kz")
with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.refresh()

# driver.get("https://hh.kz/account/login?backurl=%2F")

# element = driver.find_element_by_class_name('account-login-actions')

# account_login_element = driver.find_element(By.CLASS_NAME, 'account-login-tile-content')
# element = account_login_element.find_element(By.CLASS_NAME,'bloko-link-switch')
# element.click()
# time.sleep(2)
# form = account_login_element.find_element(By.XPATH, '//div[2]/div[1]/form[1]')
# login_input_element = form.find_element(By.CLASS_NAME,'bloko-input').send_keys('')
# password_input_element = form.find_element(By.XPATH, '//div[2]/span[1]/input').send_keys('')
# time.sleep(2)
# button_element = form.find_element(By.XPATH, '//div[4]/div[1]/button').click()
# try:
#     element.click()
#     login_input_element = form.find_element(By.CLASS_NAME,'bloko-input').send_keys('')
#     password_input_element = form.find_element(By.XPATH, '//div[2]/span[1]/input').send_keys('')
#     button_element = form.find_element(By.XPATH, '//div[4]/div[1]/button').click()
# except Exception as e:
#     pass

# time.sleep(2)

# driver.set_page_load_timeout(5)
# driver.get('https://almaty.hh.kz/')

# driver.implicitly_wait(10)
# driver.refresh()

# vacancy_responses = driver.find_element(By.CLASS_NAME, 'HH-Supernova-Menu-ArrowAnchor').click()

main_div = driver.find_elements(
    By.XPATH,  
    '/html/body/div'
)[5]


react_root = main_div.find_element(By.ID, 'HH-React-Root')
print(react_root.get_attribute('id'))
# bloko_columns = react_root.find_element(By.XPATH, 'div[1]')
bloko_columns = react_root.find_elements(By.TAG_NAME, 'a')
bloko_columns[0].click()

# for tag in bloko_columns:
#     print(tag.get_attribute('class'))

driver.refresh()
vacancies_dashboard_tag = driver.find_element(By.CLASS_NAME, 'vacancies-dashboard-manager__vacancies')
# print(vacancies_dashboard_tag.get_attribute('class'))
adaptive_table_tags = vacancies_dashboard_tag.find_elements(By.XPATH, 'div')
# print(len(adaptive_table_tags))
# adaptive_table_items = [item for item in adaptive_table_tags if item.get_attribute('class') == 'adaptive-table-item adaptive-table-item_clickable']
# print(len(adaptive_table_items))
# adaptive_table_row_section = adaptive_table_items[0].find_element(By.XPATH, 'div[2]/div[1]/div[9]')
for i in range(len(adaptive_table_tags[2:])):
    vacancies_dashboard_tag = driver.find_element(By.CLASS_NAME, 'vacancies-dashboard-manager__vacancies')
    adaptive_table_items = vacancies_dashboard_tag.find_elements(By.XPATH, 'div')[2:]
    adaptive_table_row_section = adaptive_table_items[i].find_element(By.XPATH, 'div[2]/div[1]/div[9]')
    vacancies_response_count_tag = adaptive_table_row_section.find_element(By.TAG_NAME, 'span').click()
    # driver.refresh()
    vacancy_responses_tag = driver.find_element(By.CLASS_NAME, 'HH-Employer-VacancyResponse-BatchActions-ItemsWrapper')
    employers_tags = vacancy_responses_tag.find_elements(By.TAG_NAME, 'div')
    for element in employers_tags:
        print(element.get_attribute('data-hh-resume-hash'))
    driver.back()
# print(vacancies_response_count_tag.get_attribute('data-qa'))



# print_logo_wrapper = driver.find_element(By.CLASS_NAME, 'HH-Supernova-Search-Container supernova-navi-search-wrapper supernova-navi-search-wrapper_expanded supernova-navi-search-wrapper_employer ')
# print(print_logo_wrapper.get_attribute('class'))






# with open('cookies.pkl', 'wb') as f:
#     pickle.dump( driver.get_cookies() , f)





# driver.close()
# driver.quit()




    # json.dump(cookies, f, sort_keys=True, indent=4)

# supernova_main_content = main.find_element(By.XPATH, 'div[@class="HH-MainContent HH-Supernova-MainContent"')

# vacancy_responses = driver.find_element(
#     By.XPATH,  
#     '//html/body/div[6]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/span[1]'
# ).click()
# login_form = forms.find_element_by_class_name('bloko-form-item')
# driver = webdriver.Chrome(executable_path=EXE_PATH)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")