import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

profile = r'C:\\Users\\Lucas\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\\Users\\Lucas\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Profile 1")

driver = webdriver.Chrome(
    executable_path=r"C:\\Users\\Lucas\\Projects\\tips-crawler\\chromedriver",
    chrome_options=options
)

driver.get('https://web.telegram.org/#/im?p=g518216649')
time.sleep(5) # Let the user actually see something!

textbox_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]"
send_button_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[3]/button/span[1]"

element_textbox = driver.find_element_by_xpath(textbox_xpath)
element_textbox.send_keys('Teste do robo !')

send_button = driver.find_element_by_xpath(send_button_xpath)
send_button.click()

time.sleep(5)



driver.quit()