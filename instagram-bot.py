from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

class instagramBot:
  driver = webdriver.Chrome()

  def __init__(self):
    self.launch_browser('https://www.instagram.com/')
    time.sleep(1)

    self.login()
    time.sleep(4)

    self.dismiss_popup()
    time.sleep(2)

    self.like_first_five_posts()
    time.sleep(0.5)
    self.navigate_to_profile()
    time.sleep(3.4)
    while True:
      self.recommended_users()
      time.sleep(3)
      self.follow_first_three_users()
      time.sleep(1)
      self.click_random_user()
      time.sleep(5)

  def launch_browser(self, url):
    self.driver.get(url)

  def login(self) :
    driver = self.driver
    # Finding and filling username
    username_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
    username_input = driver.find_element_by_xpath(username_xpath)
    username_input.click()
    username_input.send_keys("xpriments")

    # Finding and filling password
    password_path = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'
    password_input = driver.find_element_by_xpath(password_path)
    password_input.click()
    password_input.send_keys("Thomas!06")

    # Submitting ...
    submit_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'
    submit_button =  driver.find_element_by_xpath(submit_xpath)
    submit_button.click()

  def dismiss_popup(self):
    driver = self.driver
    notifications_popup = driver.find_element_by_xpath('/html/body/div[4]/div/div')
    if notifications_popup:
      dismiss_xpath = '/html/body/div[4]/div/div/div[3]/button[2]'
      dismiss_button = driver.find_element_by_xpath(dismiss_xpath)
      dismiss_button.click()

  def like_first_five_posts(self):
    for x in range(1,6):
      like_xpath = f'//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[{x}]/div[2]/section[1]/span[1]/button'
      like_button = self.driver.find_element_by_xpath(like_xpath)
      like_button.click()
      time.sleep(0.7)

  def navigate_to_profile(self):
    profile_xpath = '//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[5]/header/div[2]/div[1]/div/a'
    profile_link = self.driver.find_element_by_xpath(profile_xpath)
    profile_link.click()

  def recommended_users(self):
    recommend_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[2]'
    recommend_button = self.driver.find_element_by_xpath(recommend_xpath)
    recommend_button.click()

  def click_random_post(self):
    index = random.randrange(1, 3)
    post_xpath = f'//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[{index}]/a'
    post_link = self.driver.find_element_by_xpath(post_xpath)
    post_link.click()

  def follow_first_three_users(self):
    for x in range(3, 6):
      follow_xpath = f'//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/div/div/ul/li[{x}]/div/div/div/div/button[2]'
      follow_link = self.driver.find_element_by_xpath(follow_xpath)
      follow_link.click()
      time.sleep(.5)

  def click_random_user(self):
    random_user = random.randrange(3, 7)
    random_xpath = f'//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/div/div/ul/li[{random_user}]/div/div/div/div/div[2]'
    random_user = self.driver.find_element_by_xpath(random_xpath)
    random_user.click()

instagramBot()
