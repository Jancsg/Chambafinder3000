import email
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

Account = 'jan.carlos.sg97@gmail.com'
Password = 'Romanos1011$'
Phone = '4428327680'
Chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3203875763&geoId=106262181&keywords=Google&location=M%C3%A9xico%2C%20M%C3%A9xico&refresh=true')

time.sleep(2)
sign = driver.find_element('link text', 'Iniciar sesión')
sign.click()

time.sleep(5)
email_field = driver.find_element_by_id('username')
email_field.send_keys(Account)
password_field =dirver.find_element_by_id('password')
password_field.send_keys(Password)
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements_by_css_selector('.job-card-container--clickable')

for listing in all_listings:
    print('called')
    listing.click()
    time.sleep(2)

    #Try to locate the apply button, if can't locate then skip the job

    try:
        apply_button = driver.find_element_by_css_selector('.jobs-s-apply button')
        apply_button.click()
        time.sleep()

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name('fb-single_line-text__input')
        if phone.text == '':
            phone.send_keys(Phone)
        
        submit_button  = driver.find_element_by_css_selector('footer button')

        #If the submit_button is a 'Next' button, then this is a multi-step application, so skip.
        if submit_button.get_attribute('data-control-name') == 'continue_inify':
            close_button = driver.find_element_by_class_name('artdeco-modal__dismiss')
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name('artdeco-modal__confirm-dialog-btn')[1]
            discard_button.click()
            print('Complex application, skipped.')
            continue
        else:
            submit_button.click()
        
        #Once application completed, colse the pop-up windows.
        time.sleep(2)
        close_button = driver.find_element_by_class_name('artdeco-modal__dismiss')
        close_button.click()

        #If already applied to job or job is no longer accepting applications, then skip
    except NoSuchElementException:
        print('No application button, skipped.')
        continue
time.sleep(5)
driver.quit()
