from time import sleep
from selenium import webdriver

location =  '/home/arman/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path = location)

driver.get("https://github.com/login")

click_type = driver.find_element_by_xpath('//*[@id="login_field"]')
click_type.click()
click_type.send_keys(input('whats yore Gmail? '))

click_type_password = driver.find_element_by_xpath('//*[@id="password"]')
click_type_password.click()
click_type_password.send_keys(input('whats yore password? '))

submit_list = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
submit_list.click()

driver.get('https://github.com/Armanebtekari/comit/edit/main/README.md')

commit = driver.find_element_by_xpath('//*[@id="new_blob"]/div/file-attachment/div/div[2]/div/textarea')
commit.click()
commit.send_keys('commit')

display = driver.find_element_by_xpath('//*[@id="new_blob"]/div/div[1]/span/input')
display.click()

sleep(1)
submit = driver.find_element_by_xpath('//*[@id="submit-file"]')
submit.click()

driver.get('https://github.com/Armanebtekari/comit/edit/main/README.md')

commit = driver.find_element_by_xpath('//*[@id="new_blob"]/div/file-attachment/div/div[2]/div/textarea')
commit.click()
commit.send_keys('commit')

display = driver.find_element_by_xpath('//*[@id="new_blob"]/div/div[1]/span/input')
display.click()

for x in range(10):
    sleep(1)
    submit = driver.find_element_by_xpath('//*[@id="submit-file"]')
    submit.click()

    driver.get('https://github.com/Armanebtekari/comit/edit/main/README.md')

    commit = driver.find_element_by_xpath('//*[@id="new_blob"]/div/file-attachment/div/div[2]/div/textarea')
    commit.click()
    commit.send_keys('commit')

    display = driver.find_element_by_xpath('//*[@id="new_blob"]/div/div[1]/span/input')
    display.click()
