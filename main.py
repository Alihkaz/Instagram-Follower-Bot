#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH =" YOUR CHROM DRIVER PATH"
SIMILAR_ACCOUNT = "Account you want their audience from "
USERNAME = "YOUR INSTAGRAM USERNAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"

#note: this program is for an already created account , if you dont have one , create it first manually not by selenium ,
#  and then log in automatically by the functions bellows by giving the proper data 

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)#To let the process slow and to not get banned by the instagram each time we make a click or follow . 

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal) #scrolling through the list of followers(js) 
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()




bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

#first we login , then we find the list of the followers , then we loop throgh the followers and follow each of them !
#where we will login for a one time , find followers , then follow as much as the account have followers , each time we scroll down 
# to find a new follower , if there is no followers left we exit ! 


#REMEMBER , OUR MAIN GOAL IS TO CATCH THE AUDIENCE OF AN ACCOUNT THAT HAS THE SAME BUSNISSE FIELD OF OURS !
