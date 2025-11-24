# from openpyxl import workbook
# excel_workbook = workbook()
#
# worksheet = excel_workbook.active
#
# worksheet.title = 'personal_info'
# worksheet['A1'] = 'name'
# worksheet['B1'] = 'place'
# worksheet['C1'] = 'phone number'
# worksheet['D1'] = 'email'
#
# data_list =[
#     ['aina', 'abc', 9898989899, 'aina@gmail.com'],
#     ['aina', 'abc', 9898989899, 'aina@gmail.com'],
#     ['aina', 'abc', 9898989899, 'aina@gmail.com'],
#     ['aina', 'abc', 9898989899, 'aina@gmail.com']
# ]
#
# for row in data_list:
#     worksheet.append(row)


###################################
#confirmation alert


# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.accept()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

#############################prompt alert########

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)


driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
time.sleep(2)

alert_obj = driver.switch_to.alert
alert_obj.send_keys("Aishwarya")
alert_obj.accept()





















