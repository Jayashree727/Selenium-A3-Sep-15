import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

driver.get('https://www.linkedin.com/')
time.sleep(2)

google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(google_frame)
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
driver.switch_to.parent_frame()
time.sleep(2)


microsoft_frame = driver.find_element('xpath', '//iframe[@name="microsoft_signin_iframe_1"]')
driver.switch_to.frame(microsoft_frame)
driver.find_element('xpath', '//span[text()="Continue with Microsoft"]').click()
driver.switch_to.parent_frame()
time.sleep(2)


ele = driver.find_element('xpath', '//h2[contains(text(),"Join your colleagues"]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

youtube_frame = driver.find_element('xpath', '//iframe[@name="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
driver.switch_to.frame(youtube_frame)
driver.find_element('xpath', '//button[@title="Play"]').click()
driver.switch_to.parent_frame()
time.sleep(2)

