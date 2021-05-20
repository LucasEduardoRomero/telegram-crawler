import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)


class TipScanner():
    def __init__(self, config_file):
        conf = load_config(config_file)        
        
        self.user_data_dir = f"user-data-dir={conf['user_data_dir']}"
        self.profile_dir = f"--profile-directory={conf['profile_dir']}"

        self.channels = conf['channelsId']
        self.last_msg_id = -1

        options = webdriver.ChromeOptions()
        options.add_argument(self.user_data_dir)
        options.add_argument(self.profile_dir)
        

        self.driver = webdriver.Chrome(
            executable_path=conf['executable_path'],
            chrome_options=options
        )
        self.driver.get(f"https://web.telegram.org/#/im?p={self.channels[0]}")    

    def monitor(self):            
        new_msg_xpath = ".//div[contains (@class, 'im_message_outer_wrap') and contains (@class, 'hasselect')]"
        new_message_arr = self.driver.find_elements_by_xpath(new_msg_xpath)         
        if(len(new_message_arr) > 0):      
            new_message_arr = new_message_arr[::-1]
            for n_msg in new_message_arr:
                msg_id = 0
                msg_id = n_msg.get_attribute('data-msg-id')
                if(msg_id):
                    msg_id = int(msg_id)
                    if(msg_id > self.last_msg_id):
                        self.last_msg_id = msg_id
                        print(f"\n{n_msg.text} - {msg_id}\n")
                    else:
                        return
        else:
            print("\nNenhuma Mensagem Encontrada\n")

    def scan(self):        
        self.driver.get(f"https://web.telegram.org/#/im?p={self.channels[0]}")
        
        time.sleep(5) # Let the user actually see something!

        textbox_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]"
        send_button_xpath = "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[3]/button/span[1]"

        element_textbox = self.driver.find_element_by_xpath(textbox_xpath)
        element_textbox.send_keys('Teste do robo !')

        send_button = self.driver.find_element_by_xpath(send_button_xpath)
        send_button.click()

        time.sleep(5)



        self.driver.quit()

if __name__ == "__main__":
    tips = TipScanner('config.json')    
    try:
        while True:
            tips.monitor()
            print("-------------------")
            time.sleep(2)
    except Exception as err:
        tips.driver.quit()
