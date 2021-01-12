from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint


class Bot():
    def __init__(self):
        self.login('king_instabot')
        self.like_comment_by_hashtag('memes')

    def login(self, username):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys('king_instabot')
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys('ilikepython')
        submit_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        submit_btn.click()
        sleep(5)
        not_now_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()
        sleep(5)
        second_not_now_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        second_not_now_btn.click()

    def like_comment_by_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys('#'+hashtag)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').send_keys(Keys.ENTER)
        sleep(5)

def main():
    my_bot = Bot()

if __name__ == '__main__':
    main()