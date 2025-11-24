#import time

#from selenium import webdriver
#chrome_driver = webdriver.Chrome()
#time.sleep(15)
#############################################


#initialise firefox browser
#from selenium import webdriver
#firefox_driver = webdriver.Firefox()

############################

#initialize edge browser
#from selenium import webdriver
#edge_driver = webdriver.Edge()

#############################
#from selenium import webdriver
#opts = webdriver.EdgeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Edge(opts)

#################
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

