import time
from settings import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


s = Service(get_path='C:\pyProjects\vkrofl\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get('https://vk.com')
    time.sleep(4)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.ENTER)
    time.sleep(3)

    driver.find_element(
        By.CLASS_NAME, "vkuiButton__content.vkuiText.vkuiText--sizeY-compact.vkuiText--w-2"
    ).click()
    time.sleep(1)

    driver.find_element(
        By.CSS_SELECTOR, "[data-test-id='verificationMethod_password']"
    ).click()
    time.sleep(2)


    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)
    time.sleep(3)

    # search_input = driver.find_element(By.ID, 'ts_input')
    # search_input.clear()
    # search_input.send_keys('Miami')
    # search_input.send_keys(Keys.ENTER)
    # time.sleep(10)
    #
    # my_page = driver.find_element(By.PARTIAL_LINK_TEXT, 'Мессенджер').click()
    # time.sleep(4)

    driver.get("https://vk.com/im?sel=-91050183")
    time.sleep(4)

    # try:
    #     print('view_profiles')
    #     view_profiles = driver.find_element(By.XPATH, "//*[contains(text(), 'Смотреть анкеты')]").click()
    #     time.sleep(1)
    # except:
    #     pass
    paused = False
    condition = True
    while condition:
        if not paused:
            try:
                like = driver.find_element(By.CLASS_NAME, "im_editable.im-chat-input--text._im_text")
                like.clear()
                like.send_keys('1')
                like.send_keys(Keys.ENTER)
                time.sleep(1)

                find_kapcha = driver.find_element(By.CLASS_NAME, 'box_layout')
                if find_kapcha:
                    paused = True
            except:
                pass
        else:
            kapcha_input = driver.find_element(By.CLASS_NAME, 'vkuiTypography.vkuiInput__el.vkuiText.vkuiText--sizeY-compact')
            kapcha_input.clear()
            print('вводи капчу сука: ')
            kapcha_text = input()
            kapcha_input.send_keys(kapcha_text)
            time.sleep(1)
            kapcha_input.send_keys(Keys.ENTER)
            time.sleep(1)
            paused = False

        # try:
        #     print('continue_viewing')
        #     continue_viewing = driver.find_element(By.XPATH, "//button/span[text()='Продолжить просмотр анкет']").click()
        # except:
        #     time.sleep(1)
        #     pass
        # try:
        #     print('too_much')
        #     too_much = driver.find_element(By.XPATH, "//*[contains(text(), 'Слишком много лайков за сегодня – ставь Мне нравится только тем, кто тебе действительно нравится. Загляни к нам попозже')]").click()
        #     condition = False
        # except:
        #     pass

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()









