import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-A3-1-3PM-Sep15\files_\demo.html')
# time.sleep(2)
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
# print(all_textboxes)            ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb9]
#
# data_list = ['Friends', 'Bads', 'Modern family', 'flash', 'big bang theory', 'squid game', 'Suits', 'GOT', 'Money heist']
#
# for textbox, data in zip(all_textboxes, data_list):
#     textbox.send_keys(data)

#############################################################################################################
'''
Eg2
wap tp print the shoe name and shoe price of adidas original shoes in myntra
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
#
# shoe_names = driver.find_elements('xpath', '//h4[@class="product-product"]')        ## [shoe1, shoe2, shoe3,.., shoe50]
# shoe_prices = driver.find_elements('xpath', '//div[@class="product-price"]')        ## [price1, price2, price3,..price50]
#
# for shoe, price in zip(shoe_names, shoe_prices):
#     print(shoe.text, '=', price.text)

#############################################################################################################
'''
Eg3

'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//div[@class="colour-more"]').click()
# time.sleep(2)
#
# all_colors = driver.find_elements('xpath', '//li[@class="colour-listItem"]')        ## list of web-elements     ## [wb1, wb2, wb3...wb20]
#
# for color in all_colors:
#     print(color.text)


#############################################################################################################
'''
Eg4

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.zomato.com/bangalore/delivery')
time.sleep(2)

driver.find_element('xpath', '//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('pizza')
time.sleep(2)

driver.find_element('xpath', '//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
time.sleep(2)

driver.find_element('xpath', '(//p[text()="Pizza - Delivery"])[1]').click()
time.sleep(2)

driver.find_element('xpath', '''//h4[text()="Domino's Pizza"]''').click()
time.sleep(4)

dominos_menu = driver.find_elements('xpath', '//h4[@class="sc-fZEjqe jToeOs"]')     ## [wb1, wb2, wb3, wb4,..]
items_prices = driver.find_elements('xpath', '//span[@class="sc-17hyc2s-1 cCiQWA"]')      ## [wb1, wb2, wb3, wb4,..]

for item, price in zip(dominos_menu, items_prices):
    print(item.text, '=', price.text)








