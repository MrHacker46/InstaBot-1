#!/usr/bin/env python
import time, sys, os, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Print usage
if len(sys.argv) is not 4:
    print("Usage:")
    print("  {} <username> <password> <hashtag>".format(sys.argv[0]))
    print("")
    print("Option:")
    print("  username :  your instagram username")
    print("  password :  your instagram password")
    print("  hashtag  :  the hashtag to search for and like")
    print("")
    print("Example usage:")
    print("  {} ___ch1pmunx___ password123 linux".format(sys.argv[0]))
    sys.exit(1)

class Instagram_Bot:
    # Init user data and browser
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver   = webdriver.Firefox()

    # Close browser method
    def close_browser(self):
        self.driver.close()

    # This method opens the browser, login the user, and likes pictures
    def login_user(self):
        # Open browser and navigate to URL
        print("[+] Opening browser...")
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        # Find the login button and click it
        print("[+] Finding login button")
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/']")
        login_button.click()
        time.sleep(3)

        # Find username field and insert data
        print("[+] Trying username: {}".format(self.username))
        uname = driver.find_element_by_xpath("//input[@name='username']")
        uname.clear()
        uname.send_keys(self.username)
        
        # Find password field and insert data
        print("[+] Trying password: {}".format(self.password))
        upass = driver.find_element_by_xpath("//input[@name='password']")
        upass.clear()
        upass.send_keys(self.password)

        # Push enter (RETURN KEY)
        upass.send_keys(Keys.RETURN)
        time.sleep(90)

    # This method clicks on the user photo and hearts it.
    # It then clicks the right arrow to move to the next photo <3
    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/");
        time.sleep(3)

        i=0
        while True:
            print("[+] Current photo: {}".format(i))

            # Click on the first photo
            print("[+] Trying to click the photo...")
            # photo = driver.find_element_by_xpath("//a[@href='/p/" + file_path + "/?tagged=" + hashtag + "']")
            photo = driver.find_element_by_xpath("/html/body/span/section/main/article/div[1]/div/div/div[1]/div[1]/a")
            driver.execute_script("arguments[0].click();", photo)
            time.sleep(1)

            # Try to <3 the photo
            try:
                print("[+] Trying to heart the photo...")
                photo_heart = driver.find_element_by_xpath("//span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
                photo_heart.click()
            # If already <3...
            except Exception:
                photo_next = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
                photo_next.click()
                time.sleep(1)
                i-=1

            # Goto next photo
            print("[+] Next photo...")
            photo_next = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
            photo_next.click()
            time.sleep(1)

            i+=1 
            if i >= random.randint(100, 144):
                print("[+] Reached {} <3!".format(i))
                print("[+] Sleeping for 1800 sec to avoid hitting rate limit...")
                print("[+] Time stopped: {}".format(datetime.now()))
                time.sleep(1800)

# Init user data (username, password)
instagram_user = Instagram_Bot(sys.argv[1], sys.argv[2])
print("[+] username={}, password={}".format(instagram_user.username, instagram_user.password))

try:
    # Login the user
    instagram_user.login_user()

    # Get hashtags
    hashtag = sys.argv[3]
    instagram_user.like_photo(hashtag)
    # hashtags = ["linux", "meditate", "yoga"]
    # [instagram_user.like_photo(tag) for tag in hashtags]
except KeyboardInterrupt:
    print("[+] User chose to exit the program...")
    print("[+] [CTRL+C] was pressed...")
    time.sleep(1)
